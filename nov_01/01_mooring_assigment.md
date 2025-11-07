You will be working with a mooring record from [the Ocean Observatories Initiative](https://oceanobservatories.org), specifically the "Flanking Subsurface Mooring B" of the [Global Irminger Sea Array](https://oceanobservatories.org/array/global-irminger-sea-array/).


1. From the resources above, along with information in the data file, compile a list of key metadata for the mooring, including 
    * project name
    * mooring ID
    * latitude
    * longitude
    * depth range
    * instrumentation
    * date/time of first observation
    * date/time of last observation

2. Create a Jupyter notebook for this assignment. See `map_plot_example.ipynb` for suggested packages to import.

3. Use xarray to load the data file.

4. Make a map showing your mooring location. If you want to use Python to create a map showing where your mooring is relative to the Greenland coast, all the code you need is in `map_plot_example.ipynb`. (You won't need to follow all of the steps given in the notebook because the mooring is in a fixed location.) You could also use Google Earth or another mapping tool.

5. Use gsw to calculate Absolute Salinity, Conservative Temperature, and potential density for the mooring data, and add these variables to the xarray dataset. You should [save this as a new Netcdf file](https://docs.xarray.dev/en/latest/generated/xarray.Dataset.to_netcdf.html) so that you don't have to repeat these calculations in future assignments.

6. The depth coordinates given are a "nominal depth" (in this case, the mean depth over the full mooring record), while the pressure data variable is the record of actual measured pressure at each instrument. Plot the pressure record for the shallowest instrument (index 0) with its nominal depth. How good is this estimate?

    You will be plotting the records from instruments 0, 6, and 10. Find the nominal depth for each.

7. Plot the record of absolute salinity for instruments 0, 6, and 10 on a single plot with a legend labeling each record by its nominal depth. 
    
8. Do the same for conservative temperature. 

9. What is the common characteristic of the three graphs during the winter months (January - March)? To the best of your knowledge, explain why this happens.