print("hello")
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station

def run():
    '''requirements for task 1D'''

    # Build list of stations
    stations = build_station_list()
    print (stations)

    # list of rivers with a station
    rivers = [] 
    

    for station in stations:
        temp = bool(1)
        for river in rivers:
            if station.river == river:
                temp = 0
        if temp == 1:
            rivers.append(station.river)

    print (rivers)
if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
run()