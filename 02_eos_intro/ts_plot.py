import numpy as np
import matplotlib.pyplot as plt
import gsw


def ts_plot(SA, CT, plot_data=False, num_isopycs=10, col_contour='k', sigma_round=0.25):
    """
    Plot density contours for temperature and salinity data.

    Parameters:
        SA : array-like
            Absolute Salinity [g/kg]
        CT : array-like
            Conservative Temperature [°C]
        plot_data : bool, optional
            Whether to plot the T-S data (scatter). Default is True.
        num_isopycs : int or list-like, optional
            Number of isopycnals to plot (default 10) or explicit contour levels.
        col_contour : str or RGB tuple, optional
            Color of contour lines and labels (default 'k')
        sigma_round : float, optional
            Rounding value for density levels (default 0.25)

    * original Matlab function here: https://github.com/margaretlindeman/matlab-functions/blob/master/tsPlot.m
    * converted to Python using chatgpt, september 2025
    """

    # Flatten arrays
    SA = np.ravel(SA)
    CT = np.ravel(CT)

    if SA.shape != CT.shape:
        raise ValueError("SA and CT must have the same shape.")

    # Constants
    lw_contour = 1
    col_data = (0, 0.447, 0.741)
    scat_size = 20

    # Compute grid bounds
    grid_SA = np.linspace(np.min(SA)-0.5, np.max(SA)+0.5, 100)
    grid_CT = np.linspace(np.min(CT)-0.5, np.max(CT)+0.5, 100)
    X, Y = np.meshgrid(grid_SA, grid_CT)
    grid_sigma = gsw.sigma0(X, Y)

    # Define isopycnals
    if np.isscalar(num_isopycs):
        sigma_vals = [
            gsw.sigma0(np.min(SA), np.max(CT)),
            gsw.sigma0(np.max(SA), np.min(CT))
        ]
        sigma_min = np.floor(min(sigma_vals) / sigma_round) * sigma_round
        sigma_max = np.ceil(max(sigma_vals) / sigma_round) * sigma_round
        sigma_range = sigma_max - sigma_min

        sigma_delta = round(sigma_range / num_isopycs / sigma_round) * sigma_round
        if sigma_delta == 0:
            sigma_delta = sigma_round

        v_isopycs = np.arange(sigma_min, sigma_max + sigma_delta, sigma_delta)
    else:
        # Assume array-like of contour levels
        v_isopycs = np.array(num_isopycs)

    # Plotting
    fig, ax = plt.subplots()

    h_isopycs = ax.contour(X, Y, grid_sigma, levels=v_isopycs,
                           colors=[col_contour], linewidths=lw_contour)
    ax.clabel(h_isopycs, fmt='%0.2f', colors=col_contour)

    # Scatter plot
    h_ts = None
    if plot_data:
        h_ts = ax.scatter(SA, CT, s=scat_size, c=[col_data], edgecolors='none')

    # Axis labels
    ax.set_xlabel("Absolute Salinity [g/kg]")
    ax.set_ylabel("Conservative Temperature [°C]")

