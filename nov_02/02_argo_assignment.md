# Argo float assignment 2

Reminder: you may use outside/online resources, but you must cite them!

Create a Jupyter notebook for this assignment. At the top, import any python libraries you will use and load the netCDF of your dataset that you saved last time. 

1. Plot the density anomaly record as a function of time (x-axis) and depth (y-axis).

2. Plot density anomaly contours over the record of (conservative) temperature:

    * First plot the temperature record as you did before.
    * Now plot the density anomalies as contour lines (labeled) on top of conservative temperature. Please label the contour lines. The density contours (isopycnals) should all be one color -- make sure adding these to the plot doesn't affect the colorbar scale for the temperature data. [This demo of matplotlib contour plots](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_demo.html#sphx-glr-gallery-images-contours-and-fields-contour-demo-py) shows you how to do this.
    * Show two versions of this plot: (a) the full record over all depths and (b) the full record for just the upper 400 m.

3. Calculate the mixed layer depth using density threshold method: 
    * Assume that the shallowest measurement in the profile represents the surface. Moving down from this point, we find the depth at which the density is greater than the surface density by at least 0.03 kg m^-3. This is our criterion for identifying the "mixed layer depth". (This threshold was established by [Montégut et al. 2004](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2004jc002378).)

        To do this, calculate calculate $\Delta \sigma = \sigma(z, t) - \sigma(\textrm{surface},t)$ for your entire record.

        In other words, choose the depth index corresponding to the shallowest measurement throughout the record, and subtract the density at this depth from the full density profile. At the surface, $\Delta \sigma = 0$ kg/m $^3$ by definition, and as you go down its value should increase.
    
    * Plot the full record of $\Delta \sigma$ as a function of depth/time, and then overlay a line contour plot of $\Delta \sigma$ with *just the 0.03 kg/m $^3$ contour level*. This line follows where the difference between the surface value and every other depth is 0.03 kg/m $^3$. Above this line we know the difference is less than 0.03 kg/m $^3$ (i.e. still considered part of the mixed layer), and below this line, we know that the difference is greater than 0.03 kg/m $^3$.

4. Make a figure with two subplots: (top) conservative temperature record for upper 400 m, and (bottom) absolute salinity record for upper 400 m. On both plots, add the 0.03 kg/m $^3$ contour of $\Delta \sigma$ over the plotted data. This represents the mixed layer depth.

5. Analysis - By either visually inspecting your plots or by calculating directly (see final bullet point below), please describe how the mixed layer depth varies over time and answer the following questions:

    * What is the range in mixed layer depths over time?

    * When are the deepest mixed layer depths?

    * When are the shallowest mixed layer depths?

    * How do changes in the mixed layer depth vary with temperature? With salinity?

    * Any other variability or interesting features that you notice in these plots?

    * *Optional:* You can calculate the exact mixed layer depth for each profile by finding the depth at which $\Delta \sigma$ is closest to 0.03 kg/m $^3$. One way to do this is to calculate e.g. `diff = deltasigma-0.03` for each profile and find the depth at which `diff` is at a minimum.

6. Based on [Holte et al. 2017](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2017GL073426):
    1. Why is the mixed layer depth is important, specifically in the Labrador Sea where your Argo float is located?
    2. How do the mixed layer depths that you calculated compare to Holte et al., calculations of mixed layer depth for this region? (You can just estimate based on figures in the paper).
    3. How does the Labrador Sea region compare to mixed layer depths globally?
    4. Would you characterize the Argo-based climatology described in this paper as Eulerian or Lagrangian? Why?