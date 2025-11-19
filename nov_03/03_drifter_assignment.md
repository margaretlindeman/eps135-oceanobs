# Drifter assignment 3

Reminder: you may use outside/online resources, but you must cite them!

Create a Jupyter notebook for this assignment. At the top, import any python libraries you will use and load the netCDF of your dataset.

1. Download `gebco_subpolarNA.nc` and use xarray to load the GEBCO topographic dataset for the North Atlantic
Subpolar Gyre. For your reference you can find background information about this data product on the [GEBCO website](https://www.gebco.net/)

    Units: lat = latitude (degrees N)

    lon = longitude (degrees W)
    
    elevation = elevation above mean sea surface (m)

2. Plot the elevation map as colored background shading (e.g. by using `gebco.elevation.plot()`) and then plot the drifter tracks over this (it's okay to plot all of the drifters with the same style here just to get the overall impression of where the drifter tracks are). What is the range of depths where the drifters are deployed?

2. Create a similar plot zoomed in on the drifter tracks on the southeast Greenland continental shelf. Change the colorbar limits to focus on the data from the coastal regions shallower than
1000 m around Greenland (e.g. `plt.clim(-1000,0)`). 

    * How do the ocean depths change along Greenland’s coast? 
    * Does there appear to be any relationship between the drifter tracks and the ocean bathymetry? 
    * Are there areas that are avoided by the drifters?

3. You've noted in past weeks that most of the drifters initially follow the East Greenland Current along the southeast Greenland shelf (before spreading out on the western side of Greenland). One of the core concepts in physical oceanography is the tendency of the ocean currents to flow along isobaths (i.e., lines of constant bathymetry). This is mainly due to Earth’s rotation, which influences how ocean parcels flow over or around bathymetric features. (If you are curious, watch this [demo of how rotating flows behave in the presence of an obstacle](https://www.youtube.com/watch?v=7GGfsW7gOLI).)

    * How does the shape of the continental shelf change around ~63.5ºN? Do the drifter trajectories appear to be affected by this? How? 
    
    * Revisit your map from last week with the scatterplot of drifter velocity at each location — what happens to the drifter velocities in this region? 
    
    * Why might this change in the bathymetry cause the coastal current to accelerate?


4. One feature present on Greenland’s coast are canyons, typically deeper than 200 m, that run
perpendicular to Greenland’s coast. These are called topographic troughs, and they usually
coincide with large fjords that extend inland. One of the most prominent troughs is the Sermilik
Trough located between 64.5-65.5N and 36-39W (you can [read more about the troughs around
Greenland here](https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.1029/2019GL083953)).

    Assuming the drifters are following the East Greenland Coastal Current (EGCC): 

    * Does the Sermilik Trough affect the flow of the EGCC?
    * Consider the smaller troughs downstream (further south along the coast) — which ones appear to impact the EGCC? Explain your reasoning.