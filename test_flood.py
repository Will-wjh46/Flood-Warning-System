#Tests for modules in flood.py
from floodsystem import flood
from floodsystem.stationdata import build_station_list,update_water_levels



def test_stations_level_over_threshold():
    '''test creating list of tupples containing rivers over tol'''
    stations = build_station_list()
    update_water_levels(stations)
    
    for x in range(5,10):
        tol = x/10
        output = flood.stations_level_over_threshold(stations, tol)
        for station in output:
            assert station[1] > tol


