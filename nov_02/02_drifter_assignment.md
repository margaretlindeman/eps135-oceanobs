# Surface drifter assignment 2

Reminder: you may use outside/online resources, but you must cite them!

Create a Jupyter notebook for this assignment. At the top, import any python libraries you will use and load the netCDF of your dataset that you saved last time. 

1. Estimate ocean surface currents from drifter position: 

    * Estimate the speed in m/s (speed = distance/time) of the SVP and SVPS drifters between every two consecutive coordinate points. Then build new timeseries for each drifter with velocity at each mid-point between each set of coordinate points.
        * You can use the `.diff()` function to find time elapsed between consecutive measurements, but check what units of time this is giving you and convert to seconds if necessary.
        * You can calculate distance in meters from lat-lon points using [gsw.distance](https://teos-10.github.io/GSW-Python/gsw_flat.html).

2. Map the surface currents: Use the code from last week to create a map of all of the drifter trajectories with colored scatter points along each trajectory showing the current speed at every point. (Note that [you can use `s=___` to set the marker size in your scatter plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html) --- you might have to play around with the map a bit to create a plot that is legible.)

3. Create some timeseries plots of the drifter velocities (line plot of speed on the y-axis versus time on the x-axis for each drifter). It's up to you how many plots to make and how to group them but here are some suggestions: 
    1. Create two subplots: On top, plot the SVP drifter speeds; plot the SVPS speeds on the bottom. Add a horizontal line to each plot showing the mean speed. Is there any systematic difference in drifter velocity between the two platforms?
    2. Group the drifters into at least two groups, closer and further from the coast -- how do they differ?

    Is seasonal variability in the velocities evident in any of your plots? What other questions do you have?

4. Based on your velocity maps and Figure 16 in [this paper (Sutherland and Pickart [2008])](https://www.sciencedirect.com/science/article/abs/pii/S0079661108000864), which ocean current(s) do the SVP and SVPS drifters measure? Which drifter (or drifters) measures the current’s velocity core (i.e., maximum velocities)? Where does this drifter end up?