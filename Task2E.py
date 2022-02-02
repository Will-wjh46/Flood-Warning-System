# WG Created: 1/2/22 Modified: 2/2/22
# IA Lent term computing module task 2E

from floodsystem import datafetcher, stationdata, flood, plot
from datetime import timedelta


def run():
    """Requirements for Task 2E"""

    # Build list of stations
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)

    N = 5
    dt = 10
    highest_stations = flood.stations_highest_rel_level(stations, N)
    for station in highest_stations:
        dates, levels = datafetcher.fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
        plot.plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
