# About

This is a simple python script that takes the CSV of Ottawa mortality
and produces the following image...

<a href=https://raw.githubusercontent.com/bartman/covid19-ottawa/master/plot.png>
    <img src=plot.png>
    </a>

For comparison, here is the daily Canadian all cause mortality over the last 10+ years.

<a href=https://raw.githubusercontent.com/bartman/covid19-ottawa/master/canada.png>
    <img src=canada.png>
    </a>

And Ontario all cause mortality:

<a href=https://raw.githubusercontent.com/bartman/covid19-ottawa/master/ontario.png>
    <img src=ontario.png>
    </a>

# Where did the data come from?

The Ottawa COVID-19 data came from https://www.arcgis.com/home/item.html?id=6bfe7832017546e5b30c5cc6a201091b

The Canada mortality data came from https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310076801&pickMembers%5B0%5D=3.1&cubeTimeFrame.startDaily=2019-01-01&cubeTimeFrame.endDaily=2019-12-31&referencePeriods=20190101%2C20191231

# How to plot it

Run

        ./plot.py
