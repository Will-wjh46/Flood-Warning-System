# WG Created: 2/2/22 Modified: 2/2/22
# Task 2G

"""
Criteria for flood warnings:

Severe: More than 2x the typical high value for a station for at least the last two days
High: More than 1.5x the typical high value for a station for at least two days
Moderate: More than 1x the typical high value for a station for at least two days
Low: More than 0.9x the typical high value for a station for at lest two days

"""

from floodsystem import datafetcher, stationdata, flood
from datetime import timedelta

def run():
    """Requirements for Task 2G"""

    severe_tolerance = 2
    high_tolerance = 1.5
    moderate_tolerance = 1
    low_tolerance = 0.9

    # Build list of stations
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)

    # Eliminate inconsistent stations
    consistent_stations = []
    for station in stations:
        if station.typical_range_consistent() == True and station.name != "Letcombe Bassett":
            consistent_stations.append(station)

    # Order stations by relative water level
    highest_stations = flood.stations_highest_rel_level(consistent_stations, len(consistent_stations))
    dt = 2
    data_list = []
    for station in highest_stations:
        print(station.name)
        try:
            dates, levels = datafetcher.fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
        except:
            pass
        data_list.append([station, levels])

    severe_stations = []
    high_stations = []
    moderate_stations = []
    low_stations = []

    i = 0
    # Find severe warning stations
    check_severe = True
    while check_severe == True and  i < len(data_list):
        possible = True
        for k in range(len(data_list[i][1])):
            if data_list[i][1][k] < severe_tolerance:
                possible = False
        if possible == True:
            severe_stations.append(data_list[i][0])
        else:
            check_severe = False
        i += 1

    # Find high warning stations
    check_high = True
    while check_high == True and  i < len(data_list):
        possible = True
        for k in range(len(data_list[i][1])):
            if data_list[i][1][k] < high_tolerance:
                possible = False
        if possible == True:
            high_stations.append(data_list[i][0])
        else:
            check_high = False
        i += 1

    # Find moderate warning stations
    check_moderate = True
    while check_moderate == True and  i < len(data_list):
        possible = True
        for k in range(len(data_list[i][1])):
            if data_list[i][1][k] < moderate_tolerance:
                possible = False
        if possible == True:
            moderate_stations.append(data_list[i][0])
        else:
            check_moderate = False
        i += 1

    # Find low warning stations
    check_low = True
    while check_low == True and  i < len(data_list):
        possible = True
        for k in range(len(data_list[i][1])):
            if data_list[i][1][k] < low_tolerance:
                possible = False
        if possible == True:
            low_stations.append(data_list[i][0])
        else:
            check_high = False
        i += 1

    print("The severe stations are:")
    for station in severe_stations:
        print(station.name)

    print("The high stations are:")
    for station in high_stations:
        print(station.name)

    print("The moderate stations are:")
    for station in moderate_stations:
        print(station.name)

    print("The low stations are:")
    for station in low_stations:
        print(station.name)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
