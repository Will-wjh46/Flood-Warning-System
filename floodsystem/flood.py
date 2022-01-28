'''This module allows for floods to be analysed'''

def stations_level_over_threshold(stations, tol):
    '''stations_level_over_threshold(stations, tol)
    checks if stations have a higher relative water level than tol
    outputs lists of tupples containing station data and the relative water level'''
    
    output = []
    for station in stations:
        if station.relative_water_level() == None:
            pass
        elif station.relative_water_level() > tol:
            output.append((station,station.relative_water_level()))
    return output
