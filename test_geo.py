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

