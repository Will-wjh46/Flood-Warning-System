# WG Created: 20/1/22 Modified: 24/1/22
# IA Lent term computing module task 1C

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    centre = (52.2053, 0.1218)
    r = 10 # in km
    sorted_stations = stations_within_radius(stations, centre, r)

    names = []
    for station in sorted_stations:
        names.append(station.name)
    names.sort()
    print(names)
    

    

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
