# Mooring assignment 2

Reminder: you may use outside/online resources, but you must cite them!

Create a Jupyter notebook for this assignment. At the top, import any python libraries you will use and load the netCDF of your dataset that you saved last time. 

1. Prepare data for plotting and future analysis (vertical interpolation): As you saw previously with the OSNAP data, strong currents can cause significant vertical displacements of the mooring instruments, referred to as "blowdowns." If you try to analyze temporal variability in e.g. temperature at a given depth by using the record from a single instrument, your analysis may be biased because some of the measurements were actually recorded deeper in the water column. One relatively simple way to avoid this is to interpolate the data to a uniform vertical grid. Besides mitigating blowdowns, vertical interpolation also simplifies the data analysis and future calculations.

    Use [interpolate.interp1d() from scipy.interpolate](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html) to grid your mooring data (cons. temperature, abs. salinity, $\sigma$) to 20 m bins. 

    Example code:

    `from scipy import interpolate # add this to your header`

    `# create a uniform depth vector with 20 m spacing`

    `gridded_depth = np.arange(0,ooi.depth.max(),20)`

    `# use interpolate.interp1d() to generate an interpolation function for each variable`

    `f = interpolate.interp1d(ooi.depth, [variable to interpolate, e.g. temp], bounds_error=False, fill_value=np.nan)`

    `# use the interpolation function to calculate values of the variable at the vertical points you have defined`

    `new = f(gridded_depth)`

    `plt.plot(new) # visualize the result`


2. Save gridded variables: Once you finish interpolating the data, add the gridded depth, conservative temperature, absolute salinity, potential density, and time to an xarray dataset and save as a NetCDF.

3. Plot the data: Plot the original potential temperature timeseries from CTD number 5 (mean depth ~ 180 m) against the gridded potential temperature timeseries at 180 m. How do mooring blowdowns affect the temperature records?

    Consider blowdown effect with depth: Repeat the same procedure for instruments near the surface at 40 m (CTD number 1) and in the deep ocean at 2200 m (CTD 13). Are instruments affected the same way at different depths?

4. Plotting the data: Create plots of the gridded full records of temperature, salinity and potential density with time on the x-axis and depth on the y-axis.

    Basic syntax:

    `fig,ax = plt.subplots() `
    
    `dataset.variable.plot(x='time',ax=ax)`

    (Remember to orient the y-axis so that the surface is at the top.)

5. Interpreting the data: What is happening to the water column in the upper 500 m depth (0 < z < 500 m) in terms of temperature, salinity, and density? Knowing how temperature and salinity impact water density, what is controlling the density changes after 2018? Finally, are the seawater changes below 1500 m as large as near the surface?

    (You talked about some of this in your first presentation, so you can feel free to dig more into the follow-up questions you've already identified!)