# WG Created: 1/2/22 Modified: 2/2/22
# IA Lent term computing module task 2E

from floodsystem import datafetcher, stationdata, flood, plot
from datetime import timedelta


def run():
    """Requirements for Task 2E"""

    N = 5 # Number of stations to plot
    dt = 10 # Number of days into the past to plot

    # Build list of stations
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)

    # Eliminate inconsistent stations
    consistent_stations = []
    for station in stations:
        if station.typical_range_consistent() == True and station.name != "Letcombe Bassett":
            consistent_stations.append(station)

    highest_stations = flood.stations_highest_rel_level(consistent_stations, N)
    data_list = []
    for station in highest_stations:
        dates, levels = datafetcher.fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
        data_list.append([station, dates, levels])
        
    plot.plot_water_levels(data_list, "together")


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
