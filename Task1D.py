from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station,stations_by_river

def run():
    '''requirements for task 1D'''

    # Build list of stations
    stations = build_station_list()

    rivers = rivers_with_station(stations)
    stationRiver = stations_by_river(stations)

    num = len(rivers)
    rivers = sorted(rivers)
    output = str(num) + " stations. First 10 - " + str(rivers[:10]) + "\n"
    print (output)

    def part2(river):
        output = river + " - " + str(sorted(stationRiver[river])) + "\n"
        print (output)
    
    part2("River Aire")
    part2("River Cam")
    part2("River Thames")




if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()