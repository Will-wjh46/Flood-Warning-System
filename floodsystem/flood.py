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
   
    def takeSecond(elem):
        '''Takes the second element of an array'''
        return elem[1]
    output.sort(key=takeSecond,reverse=True)
    return output



def stations_highest_rel_level(stations, N):
    '''stations_highest_rel_level(stations, N)
    sorts stations by highest relative level
    outputs highest N stations in decending order as elements in a list'''

    useable_stations = []
    for station in stations:
        if station.relative_water_level() == None:
            pass
        else:
            useable_stations.append((station,station.relative_water_level()))
    
    def takeSecond(elem):
        '''Takes the second element of an array'''
        return elem[1]
        
    useable_stations.sort(key=takeSecond,reverse=True)
    
    output = []
    for station in useable_stations:
        output.append(station[0])
    output = output[:N]

    return output