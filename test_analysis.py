# WG Created: 3/2/22 Modified: 3/2/22
# Code to test the functions within the module analysis.py


from floodsystem import analysis, stationdata, datafetcher
from datetime import timedelta
import numpy

def test_plot_water_levels():

    # Build list of stations
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)

    dt = 2 # Number of days into the past to plot
    p = 4
    dates, levels = datafetcher.fetch_measure_levels(stations[0].measure_id, dt=timedelta(days=dt))
    
    poly, d0 = analysis.polyfit(dates, levels, p)

    assert type(poly) == numpy.poly1d