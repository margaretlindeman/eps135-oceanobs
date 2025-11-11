# Ice-tethered profiler assignment 2

Reminder: you may use outside/online resources, but you must cite them!

Create a Jupyter notebook for this assignment. At the top, import any python libraries you will use and load the netCDF of your dataset that you saved last time. 

*Optional: You could download the extended ITP 121 drift timeseries through June 2025 [here](https://scienceweb.whoi.edu/itp/data/itpsys121/itp121rawlocs.dat).*

1. Estimate ocean surface currents from drifter position: 

    * Estimate the speed in m/s (speed = distance/time) between every two consecutive coordinate points. Then build new timeseries for each drifter with velocity at each mid-point between each set of coordinate points.
        * You can use the `.diff()` function to find time elapsed between consecutive measurements, but check what units of time this is giving you and convert to seconds if necessary.
        * You can calculate distance in meters from lat-lon points using [gsw.distance](https://teos-10.github.io/GSW-Python/gsw_flat.html).

2. Map the surface currents: Use your code from last week to create a (polar stereographic) map of all the ITP with colored scatter points showing the current speed at every point.

3. Plot velocity vs time. - Plot a time series of the speeds you calculated. Describe the variability of this record.

4. Read this [brief description of sea ice circulation in the Arctic Ocean](https://nsidc.org/learn/parts-cryosphere/sea-ice/science-sea-ice#anchor-patterns-of-sea-ice-movement) and the introduction of [Kaur et al., 2019](https://www.cambridge.org/core/journals/polar-record/article/panarctic-winter-drift-speeds-and-changing-patterns-of-sea-ice-motion-19792015/FA6D253BFDB540549D8AEC832D541F05) for context.

    Answer the following questions based on these resources and your plots:
    1. Why is sea ice drift and velocity an important quantity to calculate?
    2. What variables influence sea ice drift speed? What makes sea ice move faster or slower?
    3. What is the range of speeds that you calculated? When and where were the fastest speeds and when and where were some of the slowest speeds?
    4. What region is your ITP profiler in and why is its trajectory in a circular pattern?
    5. How do the speeds that you calculated compare to the speeds in the Kaur paper (Figure 1a)? Note that this study is using different units for velocity so you will need to do a unit conversion to compare values.