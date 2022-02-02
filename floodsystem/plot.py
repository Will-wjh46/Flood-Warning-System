# WG Created: 1/2/22 Modified:2/2/22
# Submodule to create plots of data created as part of Task 2E

import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    """Function to plot the water levels at a specific monitering station over time
    station must be of the class "MoiteringStation"
    dates must be a list of datetiem objects
    levels must a list that correspond to each item in dates
    does not return anything but opens a graph as a separate window"""

    # Plot
    plt.plot(dates, levels)
    plt.axhline(y = station.typical_range[0], color = 'r', linestyle = '-')
    plt.axhline(y = station.typical_range[1], color = 'g', linestyle = '-')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
