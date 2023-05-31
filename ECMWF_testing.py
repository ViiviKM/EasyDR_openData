#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open Data collection for MEPS deterministic member - WFS.

- Collect data over wfs for one or more locations (latlon)
- Collects all available parameters
- Transforms output dict into viewable dataframe

@author: kalliov
"""

import requests
import datetime as dt
import pandas as pd
from fmiopendata.wfs import download_stored_query

def collect_data(start_time, end_time):
    # Collect data
    collection_string = "fmi::forecast::harmonie::surface::point::multipointcoverage"
    latlon_1 = "60.16,24.9"
    latlon_2 = "65,21"
    snd = download_stored_query(collection_string,
                                args=["latlon=" + latlon_1,
                                      "latlon=" + latlon_2,
                                      "starttime=" + start_time,
                                      "endtime=" + end_time])
    data = snd.data
    return(data)

def reshape_dict(data, times):
    # Transform data output dict into stat-param-values form, with times separately
    # Dict to temporarily store data in new format
    new_data_dict = {}
    
    for time in times:
        # One timestep with all locations
        timestep_data = data[time]
        locations_list = list(timestep_data.keys())
        
        for location in locations_list:
            parameters = list(timestep_data[location].keys())
            # Add location and location dict into new data dict
            new_data_dict.setdefault(location, {})
        
            for param_name in parameters:
                # Take only parameter values (drop units)
                param_value = timestep_data[location][param_name]["value"]
                # Add parameter value of this timestep into list under param name
                new_data_dict[location].setdefault(param_name, []).append(param_value)
                
    return(new_data_dict, locations_list)

def main():

    #snd = download_stored_query("ecmwf::forecast::surface::point::multipointcoverage",
    #snd = download_stored_query("fmi::observations::weather::hourly::multipointcoverage")
    
    # Set start and end time for forecast collection
    now = dt.datetime.utcnow()
    start_time = now.strftime('%Y-%m-%dT00:00:00Z')
    end_time = now.strftime('%Y-%m-%dT18:00:00Z')
    
    data = collect_data(start_time, end_time)
    
    # Times to use later in forming dataframe
    times = data.keys()
    
    # Reshape dict, return also loclist for visualisations
    new_data_dict, locations_list = reshape_dict(data, times)               
                
    # Make a dataframe for each station for visualisation        
    for location in locations_list:
        location_data = new_data_dict[location]
    
        df = pd.DataFrame(index=times, data=location_data)
        print(df)

if __name__ == "__main__":
    main()