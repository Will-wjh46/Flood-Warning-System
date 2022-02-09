from floodsystem import flood
from floodsystem.stationdata import build_station_list,update_water_levels

def run():
    """Requirements for Task 2B"""
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    over_tol = flood.stations_level_over_threshold(stations, tol)
    for station in over_tol:
        print("{} {}".format(station[0].name,station[1]))



if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
