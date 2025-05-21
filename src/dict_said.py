import pandas as pd 

# Satellite ID (kx) Dictionaries 
def dict_satid(df):
    # Loop through each sat_id and plot its time series data
    # attempt 2
    cosmic2 = [750,751,752,753,754,755]
    cosmic = [740,741,742,743,744,745]
    metop = [3,4,5]
    geo_optics = [265,266]
    planet_iq = [267,268]
    champ = [41]
    metop1 = [3]
    metop2 = [4]
    metop3 = [5]
    trios_n = [205]
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
    npp = [224]
    spire = [269]

    
    
    """
    # 'other' ~ kx values not defined above
    values_to_exclude = 
    cosmic2 + cosmic + spire + metop + geo_optics + planet_iq + champ + 
    metop1 + metop2 + metop3 + npp + 
    trios_n + noaa1 + noaa2 + noaa3 + noaa4 + noaa5 + noaa6 + noaa7 + noaa8 + noaa9 + noaa10 + noaa11 + noaa12 + noaa14 + noaa15 + noaa16 + noaa17 + noaa18 + noaa19 + noaa20 + noaa21 
    """
    
    dict_kx  = dict({
        'cosmic2' : cosmic2,
        'cosmic' : cosmic,
        'spire' : spire,
        'metop' : metop,
        'geo_optics' : geo_optics,
        'planet_iq' : planet_iq,
        'champ' : champ,
        'metop1' : metop1,
        'metop2' : metop2,
        'metop3' : metop3,
        'npp' : npp,
        'trios_n' : trios_n,
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
        'noaa16' : noaa16,
        'noaa17' : noaa17,
        'noaa18' : noaa18,
        'noaa19' : noaa19,
        'noaa20' : noaa20,
        'noaa21' : noaa21,
        'other' : other
    })
    return dict_kx
