# WG Created: 2/2/22 Modified: 3/2/22
# Task 2G

"""
Criteria for flood warnings:

Each monitering staion is marked as:

Severe: More than 2x the typical high value for a station for at least the last two days
High: More than 1.5x the typical high value for a station for at least two days
Moderate: More than 1x the typical high value for a station for at least two days
Low: More than 0.9x the typical high value for a station for at lest two days

If a town has a single station, then the town will have the warning level of that station.
If a town has multiple stations, then the town will have the warning level of the highest level station, or
if a town has multiple of its most riskiest stations, then the town will have a warning level one greater.
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
    for station in highest_stations[0:100]:
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

    # Sort stations into towns
    towns_with_warnings = {} 
    for station in severe_stations:
        if station.town not in towns_with_warnings:
            towns_with_warnings[station.town] = "severe"
    for station in high_stations:
        if station.town not in towns_with_warnings:
            towns_with_warnings[station.town] = "high"
        else:
            towns_with_warnings[station.town] = "severe"
    for station in moderate_stations:
        if station.town not in towns_with_warnings:
            towns_with_warnings[station.town] = "moderate"
        else:
            towns_with_warnings[station.town] = "high"
    for station in low_stations:
        if station.town not in towns_with_warnings:
            towns_with_warnings[station.town] = "low"
        else:
            towns_with_warnings[station.town] = "moderate"
    
    for town in towns_with_warnings:
        print("{0} warning level in {1}".format(towns_with_warnings[town], town))
    


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
