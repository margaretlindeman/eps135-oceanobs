Your data set is the record from [Ice-Tethered Profiler (ITP) 121](https://www2.whoi.edu/site/itp/data/active-systems/itp-121/). Find more background information about Argo floats on the [ITP program website](https://www2.whoi.edu/site/itp/).

1. From the above resources and your data file, compile a list of key metadata for the Argo float, including 
    * ITP number
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

    On the same axes, first add a line plot of the profile longitude/latitude, and then add a scatter plot (also of the profile longitude/latitude) where the color of the scatter points is determined by the time variable. (See example code!!) Double-check that this looks similar to the track you saw on the ITP website.

    Don't forget to add a descriptive title to your plot.


8. Choose two profiles that are separated in time and/or space (maybe one in summer and one in winter). Plot the two absolute salinity and two conservative temperature profiles together. (e.g. create a figure with two subplots, left and right. On one subplot, add line plots for two individual profiles with salinity on the x-axis and pressure on the y-axis. Use `label=...` to describe each one and create a legend.)

    Describe the main similarities and differences between the two profiles. To the best of your knowledge, explain the reasons for the main differences you observe.


