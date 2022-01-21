# WG Created: 20/1/22 Modified: 21/1/22
# IA Lent term computing module task 1B

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    p = (52.2053, 0.1218)
    sorted_stations = stations_by_distance(stations, p)

    output = []
    for item in sorted_stations[:10]:
        output.append((item[0].name, item[0].town, item[1]))
    print("\nThe 10 closest monitering stations to Cambridge City Centre are:")
    print(output)

    output = []
    for item in sorted_stations[-10:]:
        output.append((item[0].name, item[0].town, item[1]))
    print("\nThe 10 furthest UK monitering stations to Cambridge City Centre are:")
    print(output)
    

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
