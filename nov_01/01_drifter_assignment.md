You will be working with ocean surface drifter records deployed as part of the [EGC DrIFT project](https://www.nioz.nl/en/about/organisation/staff/femke-de-jong). You can find more information about this platform at the [Scripps Lagrangian Drifter Lab website](https://gdp.ucsd.edu/ldl/), including specs for the [Surface Velocity Program (SVP)](https://gdp.ucsd.edu/ldl/svp/) and [SVP Salinity](https://gdp.ucsd.edu/ldl/svps/) drifter configurations. Your data set includes two files, one with SVP drifter data and one with SVPS data, but all drifters were deployed together for this project.

1. From the resources above, along with the data files, compile a list of key metadata for these drifters, including 
    * project name (what does the acronym stand for?)
    * principal investigator
    * institution
    * instrumentation
    * depth
    * date/time of first observation (find this info in data files after step 3)
    * date/time of last observation

2. Create a Jupyter notebook for this assignment. Here are the packages you will probably need to import:
    
    `import xarray as xr
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import numpy as np
    import gsw`

    `# we haven't used cartopy before in this course. There is some example code in Github showing you how to make a simple basemap using this package.
    import cartopy.crs as crs
    import cartopy.feature as cfeature`

3. Use xarray to load both drifter netcdf files.

4. For the SVPS data only, use gsw to calculate Absolute Salinity, Conservative Temperature, and potential density, and add these variables to the xarray dataset. You should [save this as a new Netcdf file](https://docs.xarray.dev/en/latest/generated/xarray.Dataset.to_netcdf.html) so that you don't have to repeat these calculations in future assignments.

5. Use the provided code from our Github to plot a "base map" of the Greenland/Canada coastlines that covers the full range (plus a little breathing room) of latitude and longitude in your data file. (You can find out the lat/lon range for each dataset in the *Attributes* of the xarray dataset, e.g. `geospatial_lat_min` --- make sure the limits you pick accommodate both sets of drifters.)

    On the map, plot a line showing each drifter track (both SVP and SVPS), and add a legend so you can find out which one belongs to which drifter. For example, for the SVP drifters, you could use a for loop to plot each one as a dotted line.

        `for x in svp.id:
            plt.plot(svp.longitude[x],svp.latitude[x],label=int(x),linestyle='dotted')`

    If you modify this code to use the same approach to plot the SVPS drifters as solid lines, you can add a legend as you have done in the past (`plt.legend()`) to distinguish between the two sets of profiles.

    Don't forget to add a descriptive title to your plot.

6. Where do the drifter tracks start? Where do they end?
    
    Identify the closest SVPS drifter to the Southeast Greenland coast and the one furthest offshore. (At times drifter tracks overlap but choose the ones that are most consistently near/far from the coast throughout the full track.)

7. Plot the two absolute salinity and two conservative temperature records together. (e.g. create a figure with two subplots, top and bottom. One one subplot, add line plots for two individual profiles with time on the x-axis and salinity on the y-axis. Use `label=...` to describe each one and create a legend.)

    Describe the main similarities and differences between the two records. To the best of your knowledge, explain the reasons for the main differences you observe.


