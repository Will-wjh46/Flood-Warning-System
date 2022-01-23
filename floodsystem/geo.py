# WG Created: 20/1/22 Modified: 21/1/22
# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
import numpy as np

def great_circle_distance(a, b):
    """great_circle_distance(a, b)
    Function to calculate the great circle distance between two points a and b (latitude, longitude)
    returns a float containing the great circle distance in km"""
    r = 6371
    h = (np.sin(np.radians(b[0] - a[0])/2)**2) + np.cos(np.radians(a[0]))*np.cos(np.radians(b[0]))*(np.sin(np.radians(b[1] - a[1])/2)**2)
    if h >= 1:
        h = 0
    d = 2*r*np.arcsin(h**(0.5))
    return d

def stations_by_distance(stations, p):
    """stations_by_distance(stations, p)
    Function to sort stations by their geographical position in km from p = (latitude, longitude)
    returns an ordered list of (stations, distance from p)"""
    tuple_list = []
    for station in stations: # Iterate through the stations
        distance = great_circle_distance(p, station.coord) # Calculate great circle distance from p
        position = 0
        if len(tuple_list) != 0:
            n = True
            while n:
                if distance > tuple_list[position][1]: # Find correct location in list to insert station
                    position += 1
                    if position == len(tuple_list):
                        n = False
                else:
                    n = False
        tuple_list = tuple_list[:position] + [(station, distance)] + tuple_list[position:] # Insert station at position
    return tuple_list

def rivers_with_station(stations):
    '''rivers_with_station(stations)
    Function to create list of all rivers with a monitering staion'''
    
    output = []
    #searches through stations to find rivers not yet included in the list
    for station in stations:
        temp = bool(1)
        for river in output:
            if station.river == river:
                temp = 0
        if temp == 1:
            output.append(station.river)
    return output

def stations_by_river(stations):
    '''stations_by_river(stations)
    sorts stations by which river they are situated on
    outputs dictionary with the key as the river name and the item as a list of stations on it'''
    output = {}
    
    rivers = rivers_with_station(stations)
    for river in rivers:
        temp = []
        for station in stations:
            if river == station.river:
                temp.append(station.name)
        output[river] = temp
    return output

#create list containing the river and how many stations in sub arrays.
def rivers_by_station_number(stations, N):
    '''rivers_by_station_number(stations, N)
    sorts rivers by how many stations are situated on them
    output in form [river,number of stations] in list'''
    rivers = rivers_with_station(stations)
    stationsLoc = stations_by_river(stations)
    output = []
    for river in rivers:
        output.append([river,int(len(stationsLoc[river]))])
    
    #sort by number of stations
    def takeSecond(elem):
        '''Takes the second element of an array'''
        return elem[1]
    output.sort(key=takeSecond,reverse=True)

    #take correct number of values
    cutoff = output[N-1][1]
    x = 0
    newOut = []
    while output[x][1] >= cutoff:
        newOut.append(output[x])
        x += 1

    return newOut