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

def test_stations_highest_rel_level():
    '''test the function stations_highest_rel_level'''
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    output = flood.stations_highest_rel_level(stations, N)
    assert len(output) == 10
    for x in range(1,9):
        assert output[x].relative_water_level() <= output[x-1].relative_water_level()


