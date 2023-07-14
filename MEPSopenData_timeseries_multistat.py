#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open Data collection for MEPS deterministic member - Timeseries.

- Collect data over the timeseries-application for one or more locations (latlon)
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

#start_time = "2022-01-01 00:00"
#end_time = "2022-01-04 00:00"

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
# Example 1. Single place
"""payload = { "place": "Kumpula",
            "starttime": start_time,
            "endtime": end_time,
            "param": parameters_str, 
            "tz": "UTC",
            "precision": "double",
            "format": "json"}"""

# Example 2. Multiple place names (note the s in places, 'place' retrieves only 1 loc)
"""payload = { "places": "Kumpula,Helsinki,Jyväskylä",
            "starttime": start_time,
            "endtime": end_time,
            "param": parameters_str, 
            "tz": "UTC",
            "precision": "double",
            "format": "json"}"""

# Example 3. Single latlon
"""payload = { "latlon": "60.169,24.938",
            "starttime": start_time,
            "endtime": end_time,
            "param": parameters_str, 
            "tz": "UTC",
            "precision": "double",
            "format": "json"}"""

# Example 4. Multiple latlon names (both latlon and latlons should work)
#               start and endtimes removed, returns a set length from now
payload = { "latlons": "60.169,24.938,62.2,25.8",
            "param": parameters_str, 
            "starttime":start_time,
            "endtime":end_time,
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

