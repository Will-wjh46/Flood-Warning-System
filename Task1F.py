from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    '''requirements for task 1F'''
    stations = build_station_list()
    invalidStations = inconsistent_typical_range_stations(stations)
    output = []
    for station in invalidStations:
        output.append(station.name)
    output = sorted(output)
    print(output)




if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()