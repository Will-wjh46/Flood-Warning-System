# WG Created: 24/1/22 Modified: 24/1/22
# Tests for the modules in geo.py


from numpy import sort
from floodsystem import geo
from floodsystem.stationdata import build_station_list

def test_great_circle_distance():
    """Test calculate the great circle distance between two points"""
    a = (52.207756, 0.117859) # London Heathrow
    b = (23.139766, 82.404865)
    distance = geo.great_circle_distance(a, b)
    assert round(distance, 2) == 7481.58

    distance2 = geo.great_circle_distance(b, a)
    assert distance == distance2


def test_stations_by_distance():
    stations = build_station_list()

    p = (52.2053, 0.1218)
    sorted_stations = geo.stations_by_distance(stations, p)
    assert len(sorted_stations[0]) == 2
    assert sorted_stations[0][0].name == 'Cambridge Jesus Lock'
    for i in range(len(sorted_stations)-1):
        assert sorted_stations[i][1] <= sorted_stations[i+1][1]

def test_stations_within_radius():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 50 # in km
    sorted_stations = geo.stations_within_radius(stations, centre, r)
    for station in sorted_stations:
        distance = geo.great_circle_distance(centre, station.coord)
        assert distance < r

def test_rivers_with_station():
    '''Test function - rivers_with_station'''
    stations = build_station_list()
    output = geo.rivers_with_station(stations)
    for x in range(0,len(output)):
        for y in range(0,len(output)):
            assert output[x] != output[y] or x == y

def test_stations_by_river():
    '''Test function - stations_by_river'''
    stations = build_station_list()
    output = geo.stations_by_river(stations)
    for item in output:
        assert len(item[1]) != 0

def test_rivers_by_station_number():
    '''Test function - rivers_by_station_number'''
    stations = build_station_list()
    for N in range(1,15):
        output = geo.rivers_by_station_number(stations, N)
        assert len(output) >= N