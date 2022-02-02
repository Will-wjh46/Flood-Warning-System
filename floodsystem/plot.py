# WG Created: 1/2/22 Modified:2/2/22
# Submodule to create plots of data created as part of Task 2E

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from floodsystem import analysis

def plot_water_levels(input, mode="together"):
    """Function to plot the water levels at specific monitering stations over time
    takes a single input which is a list of up to 6 plots to make
    each item in the list should be a list of [station, dates, levels]
    station must be of the class "MoiteringStation"
    dates must be a list of datetime objects
    levels must a list that correspond to each item in dates
    optional additional parameter "mode" to define whether to group the plots into the same window or not
    does not return anything but opens a graph as a separate window"""
    
    # Calculates how many plots are needed
    number_of_plots = len(input)
    if number_of_plots > 6:
        print("You can only enter a maximum of 6 plots at once. The first 6 have been plotted.")
        number_of_plots = 6

    for i in range(number_of_plots): # Get data from input parameter
        station = input[i][0]
        dates = input[i][1]
        levels = input[i][2]

        if mode == "together": # Groups each plot into the same window if the mode is together
            plt.subplot(1, number_of_plots, i+1)

        # Plot data
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

    return "Plot Complete"


def plot_water_level_with_fit(input, p, mode="together"):
    """Function to plot the water levels at specific monitering stations over time
    takes a single input which is a list of up to 6 plots to make
    each item in the list should be a list of [station, dates, levels]
    station must be of the class "MoiteringStation"
    dates must be a list of datetime objects
    levels must a list that correspond to each item in dates
    further parameter p which defined the degree of the polynomials
    optional additional parameter "mode" to define whether to group the plots into the same window or not
    does not return anything but opens a graph as a separate window"""
    
    # Calculates how many plots are needed
    number_of_plots = len(input)
    if number_of_plots > 6:
        print("You can only enter a maximum of 6 plots at once. The first 6 have been plotted.")
        number_of_plots = 6

    for i in range(number_of_plots): # Get data from input parameter
        station = input[i][0]
        dates = input[i][1]
        levels = input[i][2]

        if mode == "together": # Groups each plot into the same window if the mode is together
            plt.subplot(1, number_of_plots, i+1)

        poly, d0 = analysis.polyfit(dates, levels, p)

        # Plot polynomial fit at 30 points along interval
        x = matplotlib.dates.date2num(dates)
        x1 = np.linspace(x[0], x[-1], 40)
        x2 = np.linspace(x[0] - d0, x[-1] - d0, 40)
        plt.plot(x1, poly(x2), label = "Best fit polynomial")

        # Plot actual data
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

    return "Plot Complete"