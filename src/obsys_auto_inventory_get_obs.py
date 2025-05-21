import yaml
import subprocess 
from datetime import datetime
import os
import pathlib
import auto_utils as au
import random
import sys
import pandas as pd

#OBS_INV_UTILS = 
OBS_INV_YAML = '/discover/nobackup/sicohen/workenv/discover-interface/auto'
OBS_INV_CLI = '/discover/nobackup/sicohen/workenv/observation-inventory-utils/src/obs_inv_utils/obs_inv_cli.py'
OBS_INV_CLI = '/discover/nobackup/sicohen/MERRA21c/observation-inventory-utils/src/obs_inv_utils/obs_inv_cli.py'


'''
File for collecting constants and utility functions used for the automated inventory system
'''
from collections import namedtuple

#constants
NCEPLIBS_SINV = 'sinv'
NCEPLIBS_CMPBQM = 'cmpbqm'

CLEAN_PLATFORM = 'aws_s3_clean'
REANALYSIS_BUCKET = 'noaa-reanlyses-pds'
DISCOVER = 'discover'

PRIVATE_EUMETSAT_PLATFORM = 'aws_s3_private'
PRIVATE_EUMETSAT_BUCKET = 'nnja-private-eumetsat'

DATESTR_FORMAT = '%Y%m%dT%H%M%SZ'
ESCAPED_DATESTR_FORMAT = '%%Y%%m%%dT%%H%%M%%SZ'

CYCLING_6H = '21600'

InventoryInfo = namedtuple(
    'InventoryInfo',
    [   
        'obs_name',
        'key',
        'start',
        'platform',
        'cycling_interval',
        's3_bucket',
        's3_prefix',
        'bufr_files',
        'nceplibs_cmd'
    ]   
)


def parse_file(file_path):
    # List to store parsed sections
    parsed_data = []
    # Temporary list to hold a section's data
    current_section = None
    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Strip whitespace characters from the line
            line = line.strip()
            # Skip lines that start with "#"
            if line.startswith("#"):
                continue
            # Check if the line starts with "BEGIN"
            if line.startswith("BEGIN"):
                # Initialize a new section list
                current_section = []
            # Check if the line starts with "END"
            elif line.startswith("END"):
                # If there's an active section, add it to the list of parsed data
                if current_section is not None:
                    parsed_data.append(current_section)
                # Reset current_section to None
                current_section = None
            # If there's an active section, add lines to it
            elif current_section is not None:
                # Split the line based on spaces to extract components
                parts = line.split(maxsplit=2)
                #print(f'parts: {parts}')
                #print(f'line: {line}')
                if len(parts) == 3:
                    date_range = parts[0].strip()
                    cycling_interval = parts[1].strip()
                    key = parts[2].strip()
                    # Replace %y4 with %Y and so on ...
                    key = key.replace("Y%y4/M%m2", "Y%Y/M%m")
                    key = key.replace("%y4%m2%d2.%h2", "%Y%m%d.%Hz") # !!!!!!! Hz --> H
                    key = key.replace("%y2%m%d", "%y%m%d")
                    key = key.replace("%m2", "%m")
                    key = key.replace("%d2", "%d")
                    key = key.replace("%h2", "%H")
                    key = key.replace("%y4", "%Y")
                    key = key.replace("%y2", "%y")
                    key = key.replace("%Hzz", "%Hz")
                    # bufr_files for get counts meta sinv
                    bufr_files = key.split("/")[-1]
                    bufr_files = bufr_files.replace("%Y%m%d", "%")
                    bufr_files = bufr_files.replace("t%Hz", "t%z")
                    bufr_files = bufr_files.replace("%y2%m%d", "%")
                    bufr_files = bufr_files.replace("%y4%m%d", "%")
                    bufr_files = bufr_files.replace("%y%m%d", "%")
                    # Split date_range into "start" and "end"
                    start_date_str, end_date_str = date_range.split("-", 1)
                    # Convert start and end dates to the new format
                    start_date = datetime.strptime(start_date_str, "%Y%m%d_%Hz").strftime("%Y%m%dT%H%M%SZ")
                    end_date = datetime.strptime(end_date_str, "%Y%m%d_%Hz").strftime("%Y%m%dT%H%M%SZ")
                    # Redo end_datestr in case it's greater than today. This saves computing time.
                    if pd.to_datetime(end_date).strftime('%Y%m%dT%H%M%SZ') > datetime.today().strftime('%Y%m%dT%H%M%SZ'):
                        end_date = datetime.today().strftime('%Y%m%dT%H%M%SZ')
                        print(end_date)
                    # Save the parsed line as a dictionary
                    current_section.append({
                        'start': start_date,
                        'end': end_date,
                        'cycling_interval': cycling_interval,
                        'key': key,
                        'bufr_files': bufr_files,
                        'prefix': key.split("/")[-1].split(".")[0]
                    })
    return parsed_data

"""
# Example usage:
file_path = "obsys.rc"  # Path to your text file


parsed_sections = parse_file(file_path)

# Print the parsed data
for section in parsed_sections:
    print("Section:")
    for entry in section:
        print(f"  Start: {entry['start']}, End: {entry['end']}, Cycling Interval: {entry['cycling_interval']}, Key: {entry['key']}, Prefix: {entry['prefix']}")
"""

def create_get_obs_inv_yaml(section_entry):
    # populate yaml
    body = {
            'cycling_interval':au.CYCLING_6H, #21600
            'date_range': {
                'datestr':au.DATESTR_FORMAT,
                'start':section_entry['start'],
                'end':section_entry['end']
            },
            'search_info':[{
                'platform':au.DISCOVER, #.platform,
                'key':section_entry['key']
                }
            ],
        }
    
    print(f'body: {body}')
    
    #dynamic_yaml = OBS_INV_YAML + 'dynamic_get_obs_inv_'+ section_entry['prefix'] +'.yaml' 
    dynamic_yaml = section_entry['prefix'] +'_get_obs_inv.yaml' 
    yaml_file_path = os.path.join(OBS_INV_YAML, dynamic_yaml)
    
    
    with open(yaml_file_path, 'w') as file:
        yaml.dump(body, file, default_flow_style=False)

    args = ['python', OBS_INV_CLI, 'get-obs-inventory', '-c', yaml_file_path]

    return args


def create_nceplibs_sinv_inventory_yaml(section_entry, work_dir):
   # populate yaml
    body = {
        's3_bucket': ' ', #inventory_info.s3_bucket,
        's3_prefix': ' ', #inventory_info.s3_prefix,
        'date_range': {
            'datestr':au.DATESTR_FORMAT,
            'start': section_entry['start'],
            'end': section_entry['end']
        },
        'search_info':[{
            'platform':au.DISCOVER, #.platform,
            }
        ],
        'bufr_files':[section_entry['bufr_files']],
        'work_dir': work_dir,
        'scrub_files': False
    }    
    print(f'body: {body}')
    
    dynamic_yaml =section_entry['prefix'] +'_get_obs_meta_sinv.yaml' 
    yaml_file_path = os.path.join(OBS_INV_YAML, dynamic_yaml)

    
    with open(yaml_file_path, 'w') as file:
        yaml.dump(body, file, default_flow_style=False)
        
    args = ['python', OBS_INV_CLI, 'get-obs-count-meta-sinv', '-c', yaml_file_path]

    return args


def create_nceplibs_cmpbqm_inventory_yaml(section_entry, work_dir):
   # populate yaml
    body = {
        's3_bucket': ' ', #inventory_info.s3_bucket,
        's3_prefix': ' ', #inventory_info.s3_prefix,
        'date_range': {
            'datestr':au.DATESTR_FORMAT,
            'start': section_entry['start'],
            'end': section_entry['end']
        },
        'search_info':[{
            'platform':au.DISCOVER, #.platform,
            }
        ],
        'prepbufr_files':[section_entry['bufr_files']],
        'work_dir': work_dir,
        'scrub_files': False
    }    
    print(f'body: {body}')
    
    dynamic_yaml = section_entry['prefix'] +'_get_obs_meta_cmpbqm.yaml' 
    yaml_file_path = os.path.join(OBS_INV_YAML, dynamic_yaml)

    
    with open(yaml_file_path, 'w') as file:
        yaml.dump(body, file, default_flow_style=False)
        
    args = ['python', OBS_INV_CLI, 'get-obs-count-meta-cmpbqm', '-c', yaml_file_path]

    return args

# cli usage:
if __name__ == "__main__":
    #file_path = "obsys.rc"  # Path to your text file
    #file_path = "obsys.rc.loon_wnd.txt"  # Path to your text file
    #file_path = "obsys.rc.loon.MLSt.rc"
    #file_path = "obsys.1bhrs.rc"
    file_path = sys.argv[1]
    #print(f'file_path: {file_path}')
    print(sys.argv[:])
    #
    parsed_sections = parse_file(file_path)

    # Print the parsed data
    for section in parsed_sections:
        print("Section:")
        for entry in section:
            print(f' entry["key"]: {entry["key"].split("/")[-1].split(".")[0]}')#
            print(f"  Start: {entry['start']}, End: {entry['end']}, Cycling Interval: {entry['cycling_interval']}, Key: {entry['key']}")
            # Redo end_datestr in case it's greater than today. This saves computing time.
            if pd.to_datetime(entry["end"]).strftime('%Y%m%dT%H%M%SZ') > datetime.today().strftime('%Y%m%dT%H%M%SZ'):
                entry["end"] = datetime.today().strftime('%Y%m%dT%H%M%SZ')
                print(entry["end"])
            """
            #create_inv_yaml(entry)
            args = create_inv_yaml(entry)
            print(args)
            """
            #args2 = create_nceplibs_cmpbqm_inventory_yaml(entry, os.getcwd())
            #subprocess.run(args2)
            #"""
            # (1) get-obs-inventory
            args1 = create_get_obs_inv_yaml(entry)
            print(args1)
            subprocess.run(args1)
            # (2) get-obs-meta-*
            if sys.argv[2] == 'bufr':
                # (2) get-obs-meta-sinv
                args2 = create_nceplibs_sinv_inventory_yaml(entry, os.getcwd())
                subprocess.run(args2)
            elif sys.argv[2] == 'prepbufr':
                # (3) get-obs-meta-cmpbqm
                args2 = create_nceplibs_cmpbqm_inventory_yaml(entry, os.getcwd())
                subprocess.run(args2)
            else:
                print('No sinv or cmpbqm input was given. Not running get-obs-counts step.')
