#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open Data collection for MEPS deterministic member - Timeseries.

- Collect data over wfs for one or more locations (latlon)
- Collects all available parameters
- Transforms output dict into viewable dataframe

@author: kalliov
"""
import requests
import pandas as pd
import datetime as dt

pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)

# MEPS url
meps_url = "http://opendata.fmi.fi/timeseries?"

# Time to collect MEPS for
now = dt.datetime.utcnow()
start_time = now.strftime('%Y-%m-%dT00:00:00Z')
end = now + dt.timedelta(days=3)
end_time = end.strftime('%Y-%m-%dT00:00:00Z')

# Station 
station_str = "Helsinki"

# List the wanted MEPS parameters
parameters = ["name",
              "time",
              "lat", 
              "lon",
              "RadiationGlobalAccumulation",
              "T"
              ]
parameters_str = ','.join(parameters)

# List the needed parameters for the request
payload = { "latlon": "60,24,61,23",
            "starttime": start_time,
            "endtime": end_time,
            "param": parameters_str, 
            "tz": "UTC",
            "precision": "double",
            "format": "json"}

# Collect data from the server
r = requests.get(meps_url, params=payload)
data = r.json()

# Make a dataframe from the data dict
df = pd.DataFrame.from_dict(data)

# Format time
df['time'] = pd.to_datetime(df['time'])
#df['origintime'] = pd.to_datetime(df['origintime'])
df = df.set_index('time')

print(df)

