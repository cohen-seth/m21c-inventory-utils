# Satellite ID (kx) Dictionaries 
def satid_dict_gpsro(df):
    # Loop through each sat_id and plot its time series data
    # attempt 2
    cosmic2 = [750,751,752,753,754,755]
    cosmic = [740,741,742,743,744,745]
    spire = [269]
    metop = [3,4,5]
    geo_optics = [265,266]
    planet_iq = [267,268]
    champ = [41]
    
    # not in cosmic2 + cosmic + spire + metop
    values_to_exclude = cosmic2  + spire + metop + planet_iq + champ + cosmic + geo_optics 
    other = pd.unique(df[~df['sat_id'].isin(values_to_exclude)].sat_id).tolist()
    other = sorted(other)
    
    dict_gpsro = sat_groups  = dict({
        'cosmic2' : cosmic2,
        'cosmic' : cosmic,
        'spire' : spire,
        'metop' : metop,
        'geo_optics' : geo_optics,
        'planet_iq' : planet_iq,
        'champ' : champ,
        'other' : other
    })
    return dict_gpsro


def satid_dict_1bmhs(df):
    """
    
    3	METOP-1 (MetopB)
    4	METOP-2 (Metop-A)
    5	METOP-3 (Metop-C)
    """
    
    metop1 = [3]
    metop2 = [4]
    metop3 = [5]
    noaa18 = [209]
    noaa19 = [223]
    
    # not in 
    values_to_exclude = metop1 + metop2 + metop3 + noaa18 + noaa19
    other = pd.unique(df[~df['sat_id'].isin(values_to_exclude)].sat_id).tolist()
    other = sorted(other)
    
    dict_1bmhs = sat_groups  = dict({
        'metop1' : metop1,
        'metop2' : metop2,
        'metop3' : metop3,
        'noaa18' : noaa18,
        'noaa19' : noaa19,
        'other' : other
    })
    return dict_1bmhs


def satid_dict_avhrr(df):
    
    noaa18 = [209]
    noaa19 = [223]
    
    # not in 
    values_to_exclude = noaa18 + noaa19
    other = pd.unique(df[~df['sat_id'].isin(values_to_exclude)].sat_id).tolist()
    other = sorted(other)
    
    dict_avhrr = sat_groups  = dict({
        'noaa18' : noaa18,
        'noaa19' : noaa19,
        'other' : other
    })
    return dict_avhrr


def satid_dict_avcsam(df):
    # am array([206, 208,   4,   3])
    noaa15 = [206]
    noaa17 = [208]
    metop1 = [3]
    metop2 = [4]
    
    # not in 
    values_to_exclude = noaa15+noaa17+metop1+metop2
    other = pd.unique(df[~df['sat_id'].isin(values_to_exclude)].sat_id).tolist()
    other = sorted(other)
    
    dict_avcsam = sat_groups  = dict({
        'metop1' : metop1,
        'metop2' : metop2,
        'noaa15' : noaa15,
        'noaa17' : noaa17,
        'other' : other
    })
    return dict_avcsam
    

def satid_dict_avcspm(df):
    # pm array([207, 209, 223])
    noaa16 = [207]
    noaa18 = [209]
    noaa19 = [223]    
    
    # not in 
    values_to_exclude = noaa16+noaa18+noaa19
    other = pd.unique(df[~df['sat_id'].isin(values_to_exclude)].sat_id).tolist()
    other = sorted(other)
    
    dict_avcspm = sat_groups  = dict({
        'noaa16' : noaa16,
        'noaa18' : noaa18,
        'noaa19' : noaa19,
        'other' : other
    })
    return dict_avcspm

def satid_dict_1bhrs2(df):
    noaa1 = [701]
    noaa2 = [702]
    noaa3 = [703]
    noaa4 = [704]
    noaa5 = [705]
    noaa6 = [706]
    noaa7 = [707]
    noaa8 = [200]
    noaa9 = [201]
    noaa10 = [202]
    noaa11 = [203]
    noaa12 = [204]
    noaa14 = [205]
    noaa15 = [206]
    noaa16 = [207]
    noaa17 = [208]
    noaa18 = [209]
    noaa19 = [223]
    noaa20 = [225]
    noaa21 = [226]
    noaa1_21 = noaa1+noaa2+noaa3+noaa4+noaa5+noaa6+noaa7+noaa8+noaa9+noaa10+noaa11+noaa12+noaa14+noaa15+noaa16+noaa17+noaa18+noaa19+noaa20+noaa21
    
    # not in 
    values_to_exclude = noaa1+noaa2+noaa3+noaa4+noaa5+noaa6+noaa7+noaa8+noaa9+noaa10+noaa11+noaa12+noaa14+noaa15+noaa16+noaa17+noaa18+noaa19+noaa20+noaa21
    other = pd.unique(df[~df['sat_id'].isin(values_to_exclude)].sat_id).tolist()
    other = sorted(other)

    """
    satid_dict_1bhrs2 = dict_1bhrs2  = dict({
        'noaa1' : noaa1,
        'noaa2' : noaa2,
        'noaa3' : noaa3,
        'noaa4' : noaa4,
        'noaa5' : noaa5,
        'noaa6' : noaa6,
        'noaa7' : noaa7,
        'noaa8' : noaa8,
        'noaa9' : noaa9,
        'noaa10' : noaa10,
        'noaa11' : noaa11,
        'noaa12' : noaa12,
        'noaa14' : noaa14,
        'noaa15' : noaa15,
        'noaa16' : noaa16,
        'noaa17' : noaa17,
        'noaa18' : noaa18,
        'noaa19' : noaa19,
        'noaa20' : noaa20,
        'noaa21' : noaa21,
        'other' : other
    })
    """
    satid_dict_1bhrs2 = dict_1bhrs2  = dict({
        'noaa1_to_noaa21' : noaa1_21,
        'other' : other
    })
    
    return dict_1bhrs2


def satid_dict_atms(df):
    """
    
    224	NPP
    225	NOAA 20
    226	NOAA 21
    """
    
    npp = [224]
    noaa20 = [225]
    noaa21 = [226]
    
    # not in 
    values_to_exclude = npp+noaa20+noaa21
    other = pd.unique(df[~df['sat_id'].isin(values_to_exclude)].sat_id).tolist()
    other = sorted(other)
    
    dict_atms = sat_groups  = dict({
        'npp' : npp,
        'noaa20' : noaa20,
        'noaa21' : noaa21,
        'other' : other
    })
    return dict_atms


import pandas as pd
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
import os
from dict_satid import *

# For querying observations_inventory.db and extracting table(s) to a working dataframe (df)
def obs_inv_query(query,db=None): #, data_type):
    """
    db: path to database file ~ default is 'observations_inventory.db'
    query: sql query command to query the sqlite database (db)
    """

    # Connect to the database-A
    if db is None:
        db = 'm21c_observations_inventory.db'

    conn = sqlite3.connect(db)

    
    # 'query':  query = f"SELECT * FROM obs_inventory WHERE data_type LIKE '%{data_type}%' "
    # 'data_type' (For Subsetting): data_type = 'gpsro'; data_type = 'loon_wnd' ;  data_type = 'MLSt'
    
    # Execute a query and read the results into a DataFrame
    df = pd.read_sql_query(query, conn)
    df.head()
    
    # Close the connection
    conn.close()
    return df

# saving csv of empty files that were found
def export_empty_files(df, data_type):
    # save data (of empty files)
    empty_files = df[df['file_size'] <= 0]
    empty_files = empty_files[['obs_id', 'parent_dir','filename','file_size','obs_day']]
    empty_files['full_path'] = empty_files.parent_dir + empty_files.filename
    
    dest_fn = 'empty_files_datasets/plot_file_size_empty_' + str(data_type) 
    dest_path_csv = os.path.join(
        'figures', dest_fn + '.csv'
    )
    
    empty_files.to_csv(dest_path_csv)
    print(f'Total number of empty {data_type} files found: {len(empty_files)}')
    print(f'Saving empty data files to: {dest_path_csv}')

    #empty_file_message = f'Total number of empty {data_type} files found: {len(empty_files)} \n Saving empty data files to: {dest_path_csv}'
    empty_file_message_left = f'Total number of empty {data_type} files found: {len(empty_files)}'
    empty_file_message_right = f'Saving empty data files to: {dest_path_csv}' 
    
    return empty_file_message_left,empty_file_message_right


# saving plot
def export_plot(data_type):
    # save plot
    dest_fn = 'plot_m21c_' + str(data_type) 
    dest_path_png = os.path.join(
        'figures', dest_fn + '.png'
    )
    print(f'saving figure to {dest_path_png}')
    plt.savefig(dest_path_png)
    return dest_path_png
   

def plot_timeseries_file_size(data_type, db):

    # quering observation_inventory.db
    df = obs_inv_query(query = f"SELECT * FROM obs_inventory WHERE data_type LIKE '%{data_type}%'", db=db)
    df = df.sort_values(by='obs_day',ascending=True)
    #print(df)
    
    # x: always obs_day for timeseries
    # y: user input ~ 
    x = df.obs_day
    y = df['file_size']
    x = pd.to_datetime(x)
    #print(f'datetime: {x}')
    

    #families = len(pd.unique(df_filesize.data_type))
    fmly_cnt = 1 #len(families)
    
    fig, ax_sub = plt.subplots(
                    fmly_cnt, 1, sharex=True, figsize=(18,7), dpi=160)
    figure_title = f'Time Series of File Size (Mb) \n Merra 21c {data_type.upper()} Data ' 
    fig.suptitle(figure_title, y=0.98, fontsize=14)

    # empty/missing files ~ i.e. where file_size == 0 
    empty_file_message_left,empty_file_message_right = export_empty_files(df, data_type)
    #plt.suptitle(figure_title)
    plt.title(empty_file_message_left,loc='left', fontsize=11)
    plt.title(empty_file_message_right,loc='right', fontsize=11)

    mx_fl_sz = -(df['file_size'].max())
    #print(f'mx_fl_sz: {mx_fl_sz}')

    # export data used for plot?
    #df = df.sort_values(y,ascending = False)
    #df.to_csv('max_file_size.csv')
    
    
    """
    # Gb's
    ax_sub.plot(x, y/1000000, linewidth=1,
                label=data_type) #, color=colors[m_idx+2])
    """
    # Mb's
    ax_sub.plot(x, y/1000000, linewidth=1,
                label=data_type) #, color=colors[m_idx+2])

    # Missing/Empty Files
    index2=0
    missing_discover = df[(df['file_size'] == 0)]
    for i in missing_discover['obs_day']:
        # the plt lines within the conditional statements are for the label/legend
        if index2 == 0:
            plt.axvline(x=pd.to_datetime(i), color='magenta', linestyle='-',linewidth=.9, label=f'Discover Empty File (n): {len(missing_discover)}')
        else:
            plt.axvline(x=pd.to_datetime(i), color='magenta', linestyle='-',linewidth=.9)
        index2+=1
    
    # Legend
    leg = ax_sub.legend(loc='best', facecolor="white")
    
    # y axis limits
    plt.ylim((0, -mx_fl_sz*1.1/1000000))
    
    # x axis limits ~ start in 1980 end at TODAY
    date_start =  "1998-01-01 00:00:00"
    date_min = pd.to_datetime(datetime.strptime(date_start, "%Y-%m-%d %H:%M:%S"))
    date_max = pd.to_datetime(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))

    plt.xlim((date_min, date_max))
    leg_lines = leg.get_lines()
    #print(f'leg_lines: {leg_lines}')
    
    for leg_line in leg_lines:
        leg_line.set_linewidth(4)
    ##
    ax_sub.minorticks_on()
    subplot_title = f'{data_type}'
    ax_sub.text(0.01, 0.9, subplot_title,
                transform=ax_sub.transAxes, fontsize=14, backgroundcolor='white')
    ax_sub.grid(which='minor', color='lightgrey',
                linestyle='--', linewidth=0.2)
    ax_sub.grid(which='major', color='lightgrey',
                linestyle='--', linewidth=0.6)
    plt.ylabel('File Size(Mb)', fontsize=14)
    
    #plt.gcf().autofmt_xdate()
    
    plt.xlabel('Observation Datetime', fontsize=14)
    y_axis = plt.gca()
    y_axis.ticklabel_format(style='plain', axis='y')
    
    ax = plt.gca()

    fn = 'filesize_' + data_type
    dest_path_png = export_plot(fn)
    
    plt.show()
    plt.close()
    
    return dest_path_png

# Plot Timeseries observation count by day for each satellite
def plot_timeseries_obs_counts(data_type, db):
    
    # quering observation_inventory.db
    df = obs_inv_query(query = f"SELECT * FROM obs_meta_nceplibs_bufr WHERE filename LIKE '%{data_type}%'", db=db)

    # df
    if df.empty: 
        return None

    #x = "sat_id"

    # Create new 'day' variable which will be used to aggregate all 4 cycles of the day into one
    df['obs_day'] = pd.to_datetime(df['obs_day'])  # Ensure obs_day is in datetime format
    df['day'] = pd.to_datetime(df.obs_day.dt.strftime('%Y%m%d'))
    
    # Group by 'obs_day' and 'sat_id' and sum the 'obs_counts'
    grouped_df = df.groupby(['day', 'sat_id'])['obs_count'].sum().reset_index()
    #print(grouped_df)
    
    fmly_cnt = 1 #len(families)
    
    mx_ob_ct = -(grouped_df['obs_count'].max())
    #print(f'mx_fl_sz: {mx_ob_ct}')
    
    fig, ax_sub = plt.subplots(
                    fmly_cnt, 1, sharex=True, figsize=(18,7), dpi=160)
    figure_title = f'Time Series of Occultation Count for Each sat_id (group) \n MERRA 21c {data_type.upper()} Data ' #'Merra 21c GPSRO Data \nTime Series of File size' #'file_size test' #grouping.get_grouping_name()
    fig.suptitle(figure_title, y=0.98, fontsize=16)

    """     
    # Loop through each satellite id and plot its timeseries
    for sat_id in grouped_df['sat_id'].unique():
        sat_data = grouped_df[grouped_df['sat_id'] == sat_id]
        #plt.plot(sat_data['day'], sat_data['obs_count'], label=f'Satellite {sat_id}')
    """     
    if data_type == 'gpsro':
        sat_groups = satid_dict_gpsro(df)
        # Needed for grouping said's and plotting groups
        for said in sat_groups.keys():  
            #print(f'said: {said} {sat_groups[said]}')
            sat_id_data = df[df['sat_id'].isin(sat_groups[said])]
            grouped_df = sat_id_data.groupby(['day'])['obs_count'].sum().reset_index()
            ax_sub.plot(grouped_df['day'], grouped_df['obs_count'], linewidth=1,
                     label=said.upper())
    elif data_type == '1bmhs':
        sat_groups = satid_dict_1bmhs(df)
        # Needed for grouping said's and plotting groups
        for said in sat_groups.keys(): 
            sat_id_data = df[df["sat_id"].isin(sat_groups[said])]
            grouped_df = sat_id_data.groupby(['day'])['obs_count'].sum().reset_index()
            ax_sub.plot(grouped_df['day'], grouped_df['obs_count'], linewidth=1,
                     label=said.upper())
    elif data_type == '1bhrs2':
        sat_groups = satid_dict_1bhrs2(df)
        # Needed for grouping said's and plotting groups
        for said in sat_groups.keys():  
            sat_id_data = df[df["sat_id"].isin(sat_groups[said])]
            grouped_df = sat_id_data.groupby(['day'])['obs_count'].sum().reset_index()
            ax_sub.plot(grouped_df['day'], grouped_df['obs_count'], linewidth=1,
                     label=said.upper())
    elif data_type == 'atms':
        sat_groups = satid_dict_atms(df)
        # Needed for grouping said's and plotting groups
        for said in sat_groups.keys():  #[cosmic2,cosmic,spire,metop,other]:
            sat_id_data = df[df["sat_id"].isin(sat_groups[said])]
            grouped_df = sat_id_data.groupby(['day'])['obs_count'].sum().reset_index()
            ax_sub.plot(grouped_df['day'], grouped_df['obs_count'], linewidth=1,
                     label=said.upper())
    elif data_type == 'avcsam': # or data_type == 'avcspm':
        sat_groups = satid_dict_avcsam(df)
        # Needed for grouping said's and plotting groups
        for said in sat_groups.keys(): 
            sat_id_data = df[df["sat_id"].isin(sat_groups[said])]
            grouped_df = sat_id_data.groupby(['day'])['obs_count'].sum().reset_index()
            ax_sub.plot(grouped_df['day'], grouped_df['obs_count'], linewidth=1,
                     label=said.upper())
    elif data_type == 'avcspm': # or data_type == 'avcspm':
        sat_groups = satid_dict_avcspm(df)
        # Needed for grouping said's and plotting groups
        for said in sat_groups.keys(): 
            sat_id_data = df[df["sat_id"].isin(sat_groups[said])]
            grouped_df = sat_id_data.groupby(['day'])['obs_count'].sum().reset_index()
            ax_sub.plot(grouped_df['day'], grouped_df['obs_count'], linewidth=1,
                     label=said.upper())
    else:
        # Needed for grouping said's and plotting groups
        sat_unique = pd.unique(grouped_df['sat_id']).tolist()
        #print(f'sat_unique: {sat_unique}')
        for said in sat_unique:   
            sat_id_data = grouped_df[grouped_df["sat_id"] == said]
            #print(sat_id_data.head())            
            ax_sub.plot(sat_id_data['day'], sat_id_data['obs_count'], linewidth=1,
                     label=said) 
    """
    #
    sat_groups = dict_satid(df)
    # Needed for grouping said's and plotting groups
    for said in sat_groups.keys():  #[cosmic2,cosmic,spire,metop,other]:
        sat_id_data = df[df["sat_id"].isin(sat_groups[said])]
        grouped_df = sat_id_data.groupby(['day'])['obs_count'].sum().reset_index()
        ax_sub.plot(grouped_df['day'], grouped_df['obs_count'], linewidth=1,
                 label=said.upper())
    """

    #leg = ax_sub.legend(loc='best', facecolor="white")
    leg = ax_sub.legend(loc='upper left', facecolor="white",fontsize=16)

    # y axis limits
    plt.ylim((0, -mx_ob_ct*2))
    
    # x axis limits ~ start in 1980 end at TODAY
    date_start = "1998-01-01"
    date_min = pd.to_datetime(datetime.strptime(date_start, "%Y-%m-%d"))
    date_max = pd.to_datetime(datetime.today().strftime("%Y-%m-%d"))
    plt.xlim((date_min, date_max))

    leg_lines = leg.get_lines()
    
    
    for leg_line in leg_lines:
        leg_line.set_linewidth(4)
    
    ##
    ax_sub.minorticks_on()
    subplot_title = f'{data_type}'
    ax_sub.text(0.01, 0.75, subplot_title,
                transform=ax_sub.transAxes, fontsize=17, backgroundcolor='white')
    ax_sub.grid(which='minor', color='lightgrey',
                linestyle='--', linewidth=0.2)
    ax_sub.grid(which='major', color='lightgrey',
                linestyle='--', linewidth=0.6)
    #plt.ylabel('Observation Count', fontsize=15)
    plt.ylabel('Occultation Count [# day$^{-1}$]', fontsize=14)
    
    #plt.gcf().autofmt_xdate()
    
    plt.xlabel('Observation Day', fontsize=14)
    y_axis = plt.gca()
    y_axis.ticklabel_format(style='plain', axis='y')
    
    ax = plt.gca()

    # Set the font size of the x and y ticks
    ax.tick_params(axis='both', which='major', labelsize=14, width=1, length=8)
    # Customize the appearance of minor ticks
    ax.tick_params(axis='both', which='minor', width=.75, length=4)


    fn = 'obs_count_' + data_type
    dest_path_png = export_plot(fn)

    plt.show()
    plt.close()

    return dest_path_png


def get_obs_types(db):
    obs_inventory = obs_inv_query(f"SELECT * FROM obs_inventory", db)
    data_types = pd.unique(obs_inventory['data_type'])
    #print(f"obs_inventory data_type counts: \n  {out}  ") 
    return data_types

def run_inventory_plots(db=None,data_types=None):
    if data_types is None:
        data_types = input("Enter the obs type to inventory (enter '-A' for all:")
        if data_types == "-A":
            data_types = get_obs_types(db)
    """
    #data_types.remove(l2)
    l1 = data_types
    l2 = ['t00z','t06z','t12z', 't18z', 'gmi_v7_L1CR', 'amsua_disc_final', 'amsre_aqua', 'avh_wnd', 'modisw_c',
          'modisw', 'ascat', 'ers2' ,'jpl_qscat', 'gdas1', 'prepbufr', 'satwnd', 'ers2_asps20n','MLSt_v5','loon_wnd','IGRA']
    l3 = [x for x in l1 if x not in l2]
    data_types = l3
    #data_types.append('IGRA')
    """

    if db is None:
        db = input("Enter the path of the database to inventory (hit 'Enter' for default):")
        
    print(f'Generating Inventory (1) File Size & (2) Obs Counts plots by obs type for : {data_types}.')
    #data_types = ['1bamua','1bhrs3','atms','crisf4','goesfv','gpsro','mtiasi','omi','ssmisu']

    # loop through and plot each data type
    for data_type in data_types:
        print(f'Generating Inventory plots for {data_type}.')
        plot_timeseries_file_size(data_type, db)
        plot_timeseries_obs_counts(data_type, db)
        print(f'Inventory plots complete.')

#run_inventory_plots()
#run_inventory_plots(db="m21c_observations_inventory.db",data_types=['1bhrs2','1bhrs3','1bhrs4'])
#run_inventory_plots(db="m21c_observations_inventory.db",data_types=['avcsam'])

run_inventory_plots(db="m21c_observations_inventory.db", data_types=['gpsro','1bhrs2','1bhrs3','1bhrs4','1bmhs','satwnd','atms'])
                                                                    # 'IGRA','ers2','gmi_v7_L1CR','amsua_disc_final','amsre_aqua','avh_wnd','modisw_c','modisw','ascat','jpl_qscat', 'prepbufr','MLSt_v5','loon_wnd'
                                                                

#'gpsro' 'MLSt_v5' 'loon_wnd' 'IGRA' '1bhrs2' '1bhrs3'
# '1bhrs4' '1bmhs' 't00z' 't06z' 't12z' 't18z' 'gmi_v7_L1CR'
# 'amsua_disc_final' 'amsre_aqua' 'avh_wnd' 'modisw_c' 'modisw' 'ascat'
# 'ers2' ,'jpl_qscat' 'gdas1' 'prepbufr' 'satwnd' 'atms'
# 'avcsam' 'avcspm']

#run_inventory_plots(db="m21c_observations_inventory.db")