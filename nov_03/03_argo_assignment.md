
# Argo float assignment 3

Reminder: you may use outside/online resources, but you must cite them!

Create a Jupyter notebook for this assignment. At the top, import any python libraries you will use and load the netCDF of your dataset that you saved last time. 

This week you'll be calculating how the mixed layer temperature and upper ocean heat content change over time.

1) Calculate the mixed layer depth for each profile: 
    * Last week you calculated the density difference from the surface for each profile and plotted a threshold to assess the mixed layer depth visually. 
    
        Create a new Jupyter notebook for this assignment and either import this variable if you saved it, or copy the code for this calculation from your previous work.
    * For each profile, find the pressure where the density difference crosses the threshold and save this value. It is probably easiest to do this using a "for loop" to analyze each profile one by one. It may be helpful also to save the index corresponding to that pressure: e.g. if the threshold for profile `x` is crossed at 41 dbar, you might have `mld[x]=41` and `mld_index[x]=8` (because `argo.pressure[8]=41`).
    * For the purpose of this assignment you may treat pressure and depth as interchangeable — but you know this is a simplification.

2) Calculate the mean conservative temperature over the mixed layer for each profile and plot this timeseries. 

    e.g. `mld_temp[x] = argo.CT[x, 0:mld_index[x]].mean()`

    How is the mixed layer temperature changing over time? Why do you think this is?
 
3) Calculate the heat content of the upper 1000 m of the ocean for each profile.

    Ocean heat content is calculated by integrating the product of the density and temperature profiles over a given depth range and multiplying by the specific heat capacity of ocean water: $Q= C_p \int \rho T \textrm{ d}z$.

    Recall from calculus courses that a definite integral over a continuous function can be approximated
by a sum of the areas of thin rectangles underneath the curve. In your dataset, the vertical spacing in pressure is 5 dbar. Approximate that this is equivalent to 5 m spacing in depth, which you will use as the value of dz (the width of the thin rectangles). The value of the product of $\rho$\*CT at each depth is the rectangle height. So the area of each rectangle is ($\rho$\*CT)\*dz.

    Here, $\rho$ is the potential density profile (not the density anomaly — remember how these are related? make sure to use the correct one) and CT is the conservative temperature profile. Cp is the specific heat capacity of seawater, 3850 J/(kg C).

    To approximate the integral, you will sum each rectangle from the surface down to 1000 m depth.
(To avoid the missing data near the surface, start your integral at ~15 m depth.) You will then repeat this integration process for each profile (using a for loop) to create a time series of integrated heat content of the upper ocean. 

    Plot the time series of ocean heat content $Q$ versus time. What units does $Q$ have based on your calculation? Remember to include units in your axis labels.
    
    How does the ocean heat content change over time? Are there any similarities or differences to the mixed layer temperature variability? Why do you think this is?

4) Read this [short blog post](https://web.archive.org/web/20230322181323/http://acsis.ac.uk/articles/item/23-what-controls-the-climatically-important-heat-content-of-the-labrador-sea) about ocean heat content in this region. For more details, you may refer to [*Heat and Freshwater Transport through the Central Labrador Sea* (Straneo, 2006)](https://doi.org/10.1175/JPO2875.1).

    What is the significance of oceanic heat content? How does the ocean lose or gain heat? Can you relate what you see in your data to any processes discussed in the the ACSIS blog post or the Straneo (2006) paper?

5) To contextualize the heat content values you have calculated, search for information on some familiar energy sources. For example, how many joules of energy are in an iphone battery, the sun, or the power for an average US household? How does this compare to your values? Note that 1 J = 1 Watt second. Often times battery or energy specifications are listed in Watt hours (Wh) so you may have to convert units. Choose one or two examples to share in your presentation.