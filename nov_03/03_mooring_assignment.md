# Mooring assignment 3

Reminder: you may use outside/online resources, but you must cite them!

Create a Jupyter notebook for this assignment. At the top, import any python libraries you will use and load the netCDF of your gridded dataset that you saved previously.

For this assignment you will be exploring the relationship between the air temperature, heat flux and the seawater temperatures at different depth levels.

The data you’ve been working with so far is from Flanking Mooring B, which doesn’t have a surface platform. Now you’ll be adding some complementary atmospheric data from a nearby mooring (the Surface Apex mooring) For your analysis you can assume them to be at the same location.

1. Air-sea heat fluxes quantify the exchange of heat between the atmosphere
and the ocean. Read this [brief description of air-sea fluxes](https://www.whoi.edu/ocean-learning-hub/multimedia/air-sea-exchanges/). (Please include this schematic or something similar in your class presentation.) There are several different components of the heat flux; you will look at the **net** heat flux which is the sum of all of these contributions.

    To download the heat flux record from [the OOI website](https://dataexplorer.oceanobservatories.org/#go-to-data-access):
    * Select the North Atlantic: Global Irminger Sea array from the list of stations
    * Under areas of interest, select Moorings, Bulk Meteorology Instrument Package, Heat
Flux: Net Heat Flux; Go
    * Click on the Downloads tab and download the data from Package A as a csv file.
    * Make sure you save the file where you have access to it in your Jupyter Lab
    
2. Load the heat flux time series using pandas and plot the heat flux timeseries as a line plot (time on the x-axis).
    * Do the data look ok? Is there any bad data that you need to exclude (like we did with the tide gauge records)?
    * Can you figure out what positive/negative sign heat flux indicates? i.e. Is heat going into the ocean from the air a positive or negative value of heat flux? How can you tell?
    *  Describe the temporal variability in the heat flux. If the high-frequency variability is too large to see seasonal and/or interannual trends, calculate a rolling mean with an appropriate window size so that you can interpret the plot.
    * Which components of the heat flux do you think may be most important in driving the variability you observe? Refer to [Josey et al. (2018)](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2018GL080956) for more details on the contributors to heat flux in this location.

3. What is the mean heat flux in the summer months? Winter months? Annual mean?

    Is your annual mean value roughly consistent with the values in this region according to [Yu (2019)](https://www.annualreviews.org/content/journals/10.1146/annurev-marine-010816-060704)? 

4.  Plot the gridded mooring time series of conservative temperature from ~4 different depths as lines on a single plot (time on the x-axis, temperature on the y-axis, with a legend labeling each line). Include one record closest to the surface and then ~3 other depths of your choice. 

    * Is the change in ocean temperature near the surface consistent
with what you would expect given the sign, magnitude and variability of the heat flux?
Explain your conclusions.
    * Is there a depth at which the ocean temperature no longer appears connected to the surface heat flux?
    * If so, what other processes might account for variability below that depth?