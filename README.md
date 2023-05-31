# EasyDR Open Data collection

Management Viivi Kallio-Myers, Anders Lindfors

## Introduction

This GitHub repository contains examples and directions for FMI Open Data collection. The content is intended for use in the EasyDR project.

Currently examples are for collecting MEPS forecasts. Examples for collecting ECMWF forecasts through the FMI Open Data will be added soon (most likely beginning of June).

The links also include directions for collecting observations, but the examples given in this repository are only for forecasts. However, the example programs can be easily modified to collect observations.

The directions here have been written for Linux.

## Links

1. [FMI Open Data directions](https://en.ilmatieteenlaitos.fi/open-data)
This page has all the official FMI directions for the Open Data.

2. [Python directions for Open Data collection](https://github.com/pnuu/fmiopendata)
This page has the directions for collecting data thorugh WFS with python.

## Data and Parameters

The MEPS_parameters.csv contains a list of the MEPS parameters that are available on Open Data and their descriptions.

Data for single or multiple points can be collected easily with the multipointcoverage option (see example program for wfs). Gridded data can be also collected (see the wfs.html file, or directions), but this returns GRIB files. If you are unfamiliar with GRIBs, they are not trivial to work with.

## Set up information

The python directions (link 2.) has directions for installation in the beginning. Follow them to install fmiopendata and eccodes.

### wfs.html

Available data, and various options, are listed in the wfs.html file. The directions for this are given after the installation in the python directions. If this doesn't work, the wfs.html file is also included in the repository, open it with your browser. The information in the wfs.html is particularly useful for modifying the data collection example with WFS.

### Environment

The example programs were run in a mamba (or conda) environment. The environment.yaml has the list of necessary packages to collect data and run the example programs. 

The eccodes package may not be necessary, unless gridded data is wanted. With conda-forge, installing it should not be a problem.


## Example programs

- MEPSopenData_timeseries_multistat.py: 
Timeseries application example. 

- MEPSopenData_wfs_multistat.py: 
WFS example.

### Notes on the examples

1. Timeseries
- The timeseries application is used with the Smartmet database when data is collected within the FMI. The directions with Open Data and the timeseries is limited, but some help could be found in the Smartmet timeseries directions (not all directions necessarily work with open data): [Smartmet-plugin-timseries](https://github.com/fmidev/smartmet-plugin-timeseries). 
- The timeseries application does mostly the same things as the WFS does, but output and parameters are all slightly different.
- Place and latlons: Locations can be retrieved with latlons, or place names. eg. “Helsinki”, or “60,24”. The string format is strict, eg. with latlons there cannot be a space after the comma.
- Latlon and place name options are given in the example.

2. WFS
- The WFS service is quite versatile, and the python directions and FMI directions are convenient for modifying the example program.
- Place and latlons: This does not accept name or place as parameters in the same way as timeseries does, but it returns the name of the location regardless. The name can be very specific, eg. "60.1699,24.9384" gives “Central Helsinki”, "60.169,24.938" gives “Helsinki”, and "60.16,24.93" gives “Sinebrychoff park”
- Latlon and place name options are given in the example.
 
 




