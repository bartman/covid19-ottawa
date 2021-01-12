#!/usr/bin/python3
# https://www.arcgis.com/home/item.html?id=6bfe7832017546e5b30c5cc6a201091b
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import datetime
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d

# --- load ---

df = pd.read_csv("13100768.csv")

# print(df.columns)
# 'REF_DATE'
# 'GEO'
# 'DGUID'
# 'Age at time of death'
# 'Sex',
# 'Characteristics'
# 'UOM'
# 'UOM_ID'
# 'SCALAR_FACTOR'
# 'SCALAR_ID',
# 'VECTOR'
# 'COORDINATE'
# 'VALUE'
# 'STATUS'
# 'SYMBOL'
# 'TERMINATED',
# 'DECIMALS'

#for col in df.columns:
#    print(col)
#    print(df[col].unique())

#quit()

# --- cleanup ---

# reduce dataset to just useful columns
df = df.drop(columns=['DGUID', 'Characteristics', 'UOM', 'UOM_ID', 'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS'])

# drop rows with no data
df = df.dropna(subset=['VALUE'])

# cleanup REF_DATE, GEO, Age at time of death
df['REF_DATE'] = pd.to_datetime(df['REF_DATE'], yearfirst=True)
df['GEO'] = df['GEO'].str.extract(r'(.*), place of occurrence')
df['Age at time of death'] = df['Age at time of death'].str.extract(r'Age at time of death, (.*)')
#print(df)

def generate(out,geo,age,sex):

    print("---- %s ----" % out)

    # --- select ---

    df2 = df[ (df['GEO'] == geo) & (df['Age at time of death'] == age) & (df['Sex'] == sex) ]
    df2 = df2.copy()
    print(df2)

    df2['daily_deaths'] = df2['VALUE'] / 7
    df2['daily_deaths_avg'] = df2['daily_deaths'].rolling(window=5).mean()

    # --- plot ---

    date = df2['REF_DATE']
    new = df2['daily_deaths']
    avg = df2['daily_deaths_avg']

    plt.scatter(date, new, 0.5, color='orange', label='average daily deaths, reported')

    plt.plot(date, avg, linewidth=1, color='red', label='average daily deaths, 5 day average')


    # --- write out ---

    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.2)

    #plt.legend(bbox_to_anchor=(1, 0.9))
    plt.legend(loc='best')

    plt.title('%s all cause mortality, %s, %s' % (geo,age.lower(),sex.lower()))

    plt.savefig(out)

    plt.close()

# --- generate ---

generate('canada.png', 'Canada', 'all ages', 'Both sexes')
generate('ontario.png', 'Ontario', 'all ages', 'Both sexes')
