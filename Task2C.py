from floodsystem import flood
from floodsystem.stationdata import build_station_list,update_water_levels

def run():
    """Requirements for Task 2C"""
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    highest_stations = flood.stations_highest_rel_level(stations, N)
    for station in highest_stations:
        print("{} {}".format(station.name,station.relative_water_level()))




if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
