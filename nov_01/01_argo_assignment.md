Your data set is the record from Argo float 5903390 (`argo5903390.nc`). Find more background information about Argo floats on the [Argo program website](https://argo.ucsd.edu).

1. Visit the [Euro Argo monitoring dashboard](https://fleetmonitoring.euro-argo.eu/dashboard). This will show you a map and list of all currently active Argo floats in the global oceans. Use the search bar in the upper left to search for the float number above. (You will need to check the box next to *Inactive* under **Status** to make sure the result is displayed.)

    From the information on this webpage, compile a list of key metadata for the Argo float, including 
    * WMO number
    * project name
    * principal investigator
    * institution
    * instrumentation
    * date of first profile
    * date of last profile
    * depth range

2. Create a Jupyter notebook for this assignment. Here are the packages you will probably need to import:
    
    `import xarray as xr
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import numpy as np
    import gsw`

    `# we haven't used cartopy before in this course. There is some example code in Github showing you how to make a simple basemap using this package.
    import cartopy.crs as crs
    import cartopy.feature as cfeature`

3. Use xarray to load the netcdf file with your dataset. 

4. Use gsw to calculate Absolute Salinity, Conservative Temperature, and potential density, and add these variables to the xarray dataset. You should [save this as a new Netcdf file](https://docs.xarray.dev/en/latest/generated/xarray.Dataset.to_netcdf.html) so that you don't have to repeat these calculations in future assignments.

5. Plot the conservative temperature for the full float record (with time on the x-axis and pressure on the y-axis). You can use this basic syntax:

    `fig,ax = plt.subplots()
    dataset.variable.plot(x='time',ax=ax)`

    Remember to orient the y-axis so that the surface is at the top, and add clear axis labels and a title as needed. You also may choose to change the colorbar axis limits if they are not appropriate to see the variability in the data, pick a different colormap, etc.

6. Do the same for the absolute salinity data.

7. Use the provided code from our Github to plot a "base map" of the Greenland/Canada coastlines that covers the full range (plus a little breathing room) of latitude and longitude in your data file. (You can find out the lat/lon range for the dataset in the *Attributes* of the xarray dataset, e.g. `geospatial_lat_min`.)

    On the same axes, first add a line plot of the profile longitude/latitude, and then add a scatter plot (also of the profile longitude/latitude) where the color of the scatter points is determined by the time variable. (See example code!!) Double-check that this looks similar to the track you saw on the Argo monitoring dashboard page.

    Don't forget to add a descriptive title to your plot.


8. Choose two profiles that are separated in time and/or space (maybe one in summer and one in winter). Plot the two absolute salinity and two conservative temperature profiles together. (e.g. create a figure with two subplots, left and right. On one subplot, add line plots for two individual profiles with salinity on the x-axis and pressure on the y-axis. Use `label=...` to describe each one and create a legend.)

    Describe the main similarities and differences between the two profiles. To the best of your knowledge, explain the reasons for the main differences you observe.


