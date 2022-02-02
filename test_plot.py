# WG Created: 2/2/22 Modified: 2/2/22
# Tests for the functions contained within the plot.py module

from floodsystem import plot, stationdata, datafetcher
from datetime import timedelta

def test_plot_water_levels():

    # Build list of stations
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)

    dt = 2 # Number of days into the past to plot
    dates, levels = datafetcher.fetch_measure_levels(stations[0].measure_id, dt=timedelta(days=dt))
    data_list = [[stations[0], dates, levels]]
    
    plot.plot_water_levels(data_list)

    assert plot.plot_water_levels(data_list) == "Plot Complete"