# WG Created: 2/2/22 Modified:2/2/22
# File for the option tasks from milestone 1

from floodsystem import datafetcher, stationdata, analysis, plot, flood
from datetime import timedelta

def run():

    N = 5 # Number of stations to plot
    dt = 2 # Number of days into the past to plot

    # Build list of stations
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)

    # Eliminate inconsistent stations
    consistent_stations = []
    for station in stations:
        if station.typical_range_consistent() == True and station.name != "Letcombe Bassett":
            consistent_stations.append(station)

    # Get 5 stations at highest risk of flooding
    highest_stations = flood.stations_highest_rel_level(consistent_stations, N)
    data_list = []
    for station in highest_stations:
        dates, levels = datafetcher.fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
        data_list.append([station, dates, levels])
    
    plot.plot_relative_data_using_bohek(data_list)
    


if __name__ == "__main__":
    print("*** Optional Tasks: CUED Part IA Flood Warning System ***")
    run()
