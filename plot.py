#!/usr/bin/python3
# https://www.arcgis.com/home/item.html?id=6bfe7832017546e5b30c5cc6a201091b
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import datetime
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d

df = pd.read_csv("COVID-19_Cases_and_Deaths_Ottawa_EN.csv")

#print(df.columns)
#  'Date'
#  'Cumulative Cases by Episode Date'
#  'Cumulative Resolved Cases by Episode Date'
#  'Cumulative Active Cases by Episode Date'
#  'Cumulative Deaths by Date of Death'
#  'Daily Cases by Reported Date'
#  '7-day Average of Newly Reported cases by Reported Date'
#  'Daily Cases by Episode Date'
#  'Daily Cases Linked to a Community Outbreak by Episode Date'
#  'Daily Cases Linked to a School or Childcare Outbreak by Episode Date'
#  'Daily Cases Linked to an Institutional Outbreak by Episode Date'
#  'Daily Cases Not Linked to an Outbreak (i.e. Sporadic Cases) by Episode Date'
#  'Cases Newly Admitted to Hospital'
#  'Cases Currently in Hospital'
#  'Cases Currently in ICU'
#  'Cumulative Rate for 0-9 Years (per 100,000 pop) by Episode Date'
#  'Cumulative Rate for 10-19 Years (per 100,000 pop) by Episode Date'
#  'Cumulative Rate for 20-29 Years (per 100,000 pop) by Episode Date'
#  'Cumulative Rate for 30-39 Years (per 100,000 pop) by Episode Date'
#  'Cumulative Rate for 40-49 Years (per 100,000 pop) by Episode Date'
#  'Cumulative Rate for 50-59 Years (per 100,000 pop) by Episode Date'
#  'Cumulative Rate for 60-69 Years (per 100,000 pop) by Episode Date'
#  'Cumulative Rate for 70-79 Years (per 100,000 pop) by Episode Date'
#  'Cumulative Rate for 80-89 Years (per 100,000 pop) by Episode Date'
#  'Cumulative Rate for 90 Years and Over (per 100,000 pop) by Episode Date'
#  'Cumulative Rate for Males (per 100,000 pop) by Episode Date'
#  'Cumulative Rate for Females (per 100,000 pop) by Episode Date'
#  'Source of Infection is Close Contact by Episode Date'
#  'Source of Infection is Missing by Episode Date'
#  'Source of Infection is an Outbreak by Episode Date'
#  'Source of Infection is Travel by Episode Date'
#  'Source of Infection is Unknown by Episode Date'
#  'Sum of Non-Institutional Source of Infection Over the Last 14 Days'
#  '% No Known Source for Cases with Non-Institutional Source of Infection Over the Last 14 Days'

date = pd.to_datetime(df['Date'], yearfirst=True)
deaths = df['Cumulative Deaths by Date of Death']

df['newdeaths'] = df['Cumulative Deaths by Date of Death'].diff().fillna(0)

plt.scatter(date, df['newdeaths'], 0.5, color='orange', label='daily COVID-19 deaths, reported')

df['newdeathsavg'] = df['newdeaths'].rolling(window=5).mean().fillna(0)
newdeathsavg = df['newdeathsavg']

#plt.plot(date, deaths)
plt.plot(date, newdeathsavg, linewidth=1, color='red', label='daily COVID-19 deaths, 5 day average')

# ----

#date_num = dates.date2num(date)
#date_num_smooth = np.linspace(date_num.min(), date_num.max(), 30)
#newdeaths_spl = make_interp_spline(date_num, newdeaths, k=3)
#newdeaths_smooth = newdeaths_spl(date_num_smooth)
#plt.plot(dates.num2date(date_num_smooth), newdeaths_smooth)

# ----

#date_num_smooth = np.linspace(date_num.min(), date_num.max(), 100)
#newdeaths_int = interp1d(date_num, newdeaths)
#newdeaths_smooth = newdeaths_int(date_num_smooth)
#plt.plot(dates.num2date(date_num_smooth), newdeaths_smooth)

# ----

# Canadian death rate is 7.6 per 1000 (2019)
# https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310071001
ott_death_per_1000 = 7.6

# Ottawa Population 1393000
# https://www.macrotrends.net/cities/20387/ottawa-gatineau/population
ott_population = 1393000

# expected death rate
ott_exp_anual_deaths = ott_population / 1000 * ott_death_per_1000
ott_exp_avg_deaths = ott_exp_anual_deaths / 365

plt.hlines(y=ott_exp_avg_deaths, xmin=min(date), xmax=max(date), linestyles='--', label='total expected avergage daily deaths (%.2f)' % ott_exp_avg_deaths)

# ----

plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.2)

plt.legend(bbox_to_anchor=(1, 0.9))

plt.title('Ottawa laboratory confirmed COVID-19 deaths')

plt.savefig('plot.png')
