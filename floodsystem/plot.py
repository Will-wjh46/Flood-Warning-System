# WG Created: 1/2/22 Modified:2/2/22
# Submodule to create plots of data created as part of Task 2E

import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from floodsystem.station import MonitoringStation

def plot_water_levels(input, mode="together"):
    """Function to plot the water levels at specific monitering stations over time
    takes a single input which is a list of up to 6 plots to make
    each item in the list should be a list of [station, dates, levels]
    station must be of the class "MoiteringStation"
    dates must be a list of datetime objects
    levels must a list that correspond to each item in dates
    optional additional parameter "mode" to define whether to group the plots into the same window or not
    does not return anything but opens a graph as a separate window"""
    
    number_of_plots = len(input)

    for i in range(number_of_plots): # Get data from input parameter
        station = input[i][0]
        dates = input[i][1]
        levels = input[i][2]

        if mode == "together": # Groups each plot into the same window if the mode is together
            plt.subplot(1, number_of_plots, i+1)

        plt.plot(dates, levels, label = "Water level")
        plt.axhline(y = station.typical_range[0], color = 'g', linestyle = 'dashdot', label = "Typical low level")
        plt.axhline(y = station.typical_range[1], color = 'r', linestyle = 'dashdot', label = "Typical high level")

        # Add axis labels, rotate date labels, add plot title and add a legend
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45)
        plt.title(station.name)
        plt.legend()

        if mode != "together": # Show each plot separately if the mode is not together
            plt.tight_layout()  # This makes sure plot does not cut off date labels
            plt.show()

    if mode == "together":
        plt.tight_layout()  # This makes sure plot does not cut off date labels
        plt.show()
