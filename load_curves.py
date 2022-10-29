# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:14:58 2019

@author: mmarczuk
"""

import numpy as np
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta


###Set parameters
quotes_file           = 'quotes.csv'
calibrations_file     = 'calibrations.csv'
quotes_colnames       = ['Validation Date', 'Symbology', 'Ticker', 'Field Name', 'Value']
calibrations_colnames = ['Curve Name', 'Tenor', 'Symbology', 'Ticker', 'Field Name', \
                         'Instrument Type', 'Convention', 'Time', 'Spread']

curve_date = '2018-06-29'
curve_name = 'EUR-DSC'

tenors = {'ON': 1, '1W': 1, '2W': 2, '3W': 3, '1M': 1, '2M': 2, '3M': 3, '4M': 4, '5M': 5,'6M': 6, \
          '7M': 7, '8M': 8, '9M': 9, '10M': 10, '11M': 11, '1Y': 1, '15M': 15, '18M': 18, \
          '21M': 21, '2Y': 2, '3Y': 3, '4Y': 4,'5Y': 5, '6Y': 6, '7Y': 7, '8Y': 8, '9Y': 9, \
          '10Y': 10, '11Y': 11, '12Y': 12, '13Y': 13, '14Y': 14, '15Y': 15, '16Y': 16, '17Y': 17, \
          '18Y': 18, '19Y': 19, '20Y': 20, '21Y': 21, '22Y': 22, '23Y': 23, '24Y': 24, '25Y': 25, \
          '26Y': 26,'27Y': 27, '28Y': 28, '29Y': 29, '30Y': 30, '31Y': 31, '32Y': 32, '33Y': 33, \
          '34Y': 34, '35Y': 35, '36Y': 36, '37Y': 37, '38Y': 38, '39Y': 39, '40Y': 40, '41Y': 41, \
          '42Y': 42, '43Y': 43, '44Y': 44, '45Y': 45, '46Y': 46, '47Y': 47, '48Y': 48, '49Y': 49,'50Y': 50}


###Import data from files
quotes       = pd.read_csv(quotes_file, names=quotes_colnames, header=0, comment=';')
calibrations = pd.read_csv(calibrations_file, names=calibrations_colnames, header=0, comment=';')


###Data preparation
curve_date = dt.datetime.strptime(curve_date, '%Y-%m-%d').date()
quotes     = quotes.dropna(axis = 0, how='all')
quotes     = quotes.drop(['Symbology','Field Name'], axis=1)

calibrations = calibrations.dropna(axis = 0, how='all')
calibrations = calibrations.drop(['Symbology','Field Name', 'Convention', 'Time', 'Spread', ], axis=1)

quotes_on_date        = quotes[quotes['Validation Date'] == curve_date.strftime('%Y-%m-%d')]
calibrations_on_curve = calibrations[calibrations['Curve Name'] == curve_name]
calibrations_on_curve = calibrations_on_curve.reset_index(drop=True)

curve_table = calibrations_on_curve.merge(quotes_on_date, on='Ticker')


###Create timeseries
def date_by_adding_business_days(from_date, add_days):
    business_days_to_add = add_days
    current_date = from_date
    while business_days_to_add > 0:
        current_date += dt.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date

find_index_10Y = curve_table[curve_table['Tenor'] == '10Y'].index[0]
find_index_15Y = curve_table[curve_table['Tenor'] == '15Y'].index[0]
find_index_20Y = curve_table[curve_table['Tenor'] == '20Y'].index[0]
find_index_30Y = curve_table[curve_table['Tenor'] == '30Y'].index[0]

###Insert rows with ON tenor
curve_table.loc[-1] = [curve_name, 'ON', 'EUR-OIS-ON', 'OIS', curve_date, np.nan]


###Insert rows between tenors 10Y - 15Y
curve_table.loc[find_index_10Y+0.1] = [curve_name, '11Y', 'EUR-OIS-11Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_10Y+0.2] = [curve_name, '12Y', 'EUR-OIS-12Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_10Y+0.3] = [curve_name, '13Y', 'EUR-OIS-13Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_10Y+0.4] = [curve_name, '14Y', 'EUR-OIS-14Y', 'OIS', curve_date, np.nan]


###Insert rows between tenors 15Y - 20Y
curve_table.loc[find_index_15Y+0.1] = [curve_name, '16Y', 'EUR-OIS-16Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_15Y+0.2] = [curve_name, '17Y', 'EUR-OIS-17Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_15Y+0.3] = [curve_name, '18Y', 'EUR-OIS-18Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_15Y+0.4] = [curve_name, '19Y', 'EUR-OIS-19Y', 'OIS', curve_date, np.nan]


###Insert rows between tenors 20Y - 30Y
curve_table.loc[find_index_20Y+0.02] = [curve_name, '21Y', 'EUR-OIS-21Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_20Y+0.03] = [curve_name, '22Y', 'EUR-OIS-22Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_20Y+0.04] = [curve_name, '23Y', 'EUR-OIS-23Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_20Y+0.05] = [curve_name, '24Y', 'EUR-OIS-24Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_20Y+0.06] = [curve_name, '25Y', 'EUR-OIS-25Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_20Y+0.07] = [curve_name, '26Y', 'EUR-OIS-26Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_20Y+0.08] = [curve_name, '27Y', 'EUR-OIS-27Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_20Y+0.09] = [curve_name, '28Y', 'EUR-OIS-28Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_20Y+0.10] = [curve_name, '29Y', 'EUR-OIS-29Y', 'OIS', curve_date, np.nan]


###Insert rows between tenors 20Y - 30Y
curve_table.loc[find_index_30Y+0.02] = [curve_name, '31Y', 'EUR-OIS-31Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.03] = [curve_name, '32Y', 'EUR-OIS-32Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.04] = [curve_name, '33Y', 'EUR-OIS-33Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.05] = [curve_name, '34Y', 'EUR-OIS-34Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.06] = [curve_name, '35Y', 'EUR-OIS-35Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.07] = [curve_name, '36Y', 'EUR-OIS-36Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.08] = [curve_name, '37Y', 'EUR-OIS-37Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.09] = [curve_name, '38Y', 'EUR-OIS-38Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.10] = [curve_name, '39Y', 'EUR-OIS-39Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.11] = [curve_name, '40Y', 'EUR-OIS-40Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.12] = [curve_name, '41Y', 'EUR-OIS-41Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.13] = [curve_name, '42Y', 'EUR-OIS-42Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.14] = [curve_name, '43Y', 'EUR-OIS-43Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.15] = [curve_name, '44Y', 'EUR-OIS-44Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.16] = [curve_name, '45Y', 'EUR-OIS-45Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.17] = [curve_name, '46Y', 'EUR-OIS-46Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.18] = [curve_name, '47Y', 'EUR-OIS-47Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.19] = [curve_name, '48Y', 'EUR-OIS-48Y', 'OIS', curve_date, np.nan]
curve_table.loc[find_index_30Y+0.20] = [curve_name, '49Y', 'EUR-OIS-49Y', 'OIS', curve_date, np.nan]

curve_table['Validation Date'] = pd.to_datetime(curve_table['Validation Date']).dt.date

###Create timeseries
for i, row in curve_table.iterrows():
    for key, value in tenors.items():
        if row['Tenor'] == key:
            if key == 'ON':
                curve_table.at[i,'Start Date'] = curve_date
            else:
                curve_table.at[i,'Start Date'] = date_by_adding_business_days(curve_date,2)
               
#curve_table['Start Date'] = date_by_adding_business_days(curve_date,2)
curve_table = curve_table.sort_index().reset_index(drop=True)

for i, row in curve_table.iterrows():
    for key, value in tenors.items():
        if row['Tenor'] == key:
            if key == 'ON':
                curve_table.at[i,'End Date'] = date_by_adding_business_days(curve_date,1)
            if key[-1] == 'W':    
                curve_table.at[i,'End Date'] = row['Start Date'] + relativedelta(weeks=value) 
            if key[-1] == 'M':    
                curve_table.at[i,'End Date'] = row['Start Date'] + relativedelta(months=value) 
            if key[-1] == 'Y':    
                curve_table.at[i,'End Date'] = row['Start Date'] + relativedelta(years=value)

###Interpolation       
curve_table['Value'] = curve_table['Value'].interpolate(method = "linear", order = 1,  limit_direction = "both", \
                                                        downcast = "infer")


###Add column with year fractions
for i, row in curve_table.iterrows():
    for key, value in tenors.items():
        find_index_2Y = curve_table[curve_table['Tenor'] == '2Y'].index[0]
        if i < find_index_2Y:
            curve_table.at[i,'Year Fraction'] = ((row['End Date'] - row['Start Date']).days)/365
        else:
            curve_table.at[i,'Year Fraction'] = ((row['End Date'] - curve_table.iloc[i-1]['End Date']).days)/365


###Reorder columns
curve_table_cols = list(curve_table.columns)
curve_table_cols = [curve_table_cols[4]] + [curve_table_cols[-3]] + [curve_table_cols[-2]] \
                    + [curve_table_cols[0]] + [curve_table_cols[2]] + [curve_table_cols[1]] \
                    + [curve_table_cols[3]] + [curve_table_cols[5]] + [curve_table_cols[8]]         
curve_table      = curve_table[curve_table_cols]


###Add column with discount factors
for i, row in curve_table.iterrows():
    find_index_1Y = curve_table[curve_table['Tenor'] == '1Y'].index[0]
    if i <= find_index_1Y:
        curve_table.at[i,'Discount Factor'] = 1 / (1 + row['Value'] * row['Year Fraction'])
    else:
        curve_table.at[find_index_1Y,'Recursion'] = 0
        curve_table.at[i,'Recursion']   = curve_table.iloc[i-1]['Discount Factor'] * curve_table.iloc[i-1]['Year Fraction'] + curve_table.iloc[i-1]['Recursion']
        curve_table.at[i,'Discount Factor'] = (1 - row['Value'] * (curve_table.iloc[i]['Recursion'])) / (1 + row['Value'] * ((row['End Date'] - curve_table.iloc[i-1]['End Date']).days)/365)

curve_table = curve_table.drop(['Recursion'], axis=1)


###Add column with zero rates
curve_table['Zero Rate'] = -np.log(curve_table['Discount Factor']) / curve_table['Year Fraction']


###Save curve to Excel
curve_table.to_excel(curve_name + '_' + curve_date.strftime('%Y%m%d') + '.xlsx', sheet_name=curve_name, index=False)