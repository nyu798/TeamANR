#!/usr/bin/env python

import sys
import json
import datetime
import numpy
import matplotlib
import urllib2
from rtree import index as rtree
from matplotlib.path import Path
from shapely.geometry import Point, shape

sys.path.append('.')

# Filtering by checking the validity of the location
def checkLocationValidity(location):
    try:
        if(location[0] != 0 and location[1] != 0):
            return True
        else:
            return False
    except:
        print >> sys.stderr, ("Location Invalid", location)
        return False
		
# Check the validity of pickup and dropoff time
def comparePickDropTime(pickup, dropoff):
    try:
        pickup_date, pickup_time = pickup.split(' ')
        pickup_year, pickup_month, pickup_day = pickup_date.split('-')
        pickup_hour, pickup_minute, pickup_sec = pickup_time.split(':')
        
        dropoff_date, dropoff_time = dropoff.split(' ')
        dropoff_year, dropoff_month, dropoff_day = dropoff_date.split('-')
        dropoff_hour, dropoff_minute, dropoff_sec = dropoff_time.split(':')
		
        return (datetime.datetime(int(pickup_year), int(pickup_month), int(pickup_day), int(pickup_hour), int(pickup_minute), int(pickup_sec))) < (datetime.datetime(int(dropoff_year), int(dropoff_month), int(dropoff_day), int(dropoff_hour), int(dropoff_minute), int(dropoff_sec)))
    except:
        print >> sys.stderr, (pickup, dropoff)
        return False

def readNeighborhoodData(shape_file, index, neighborhoods):
    for entry in shape_file:
        paths = map(Path, entry['geometry']['coordinates'])
        bbox = paths[0].get_extents()
        map(bbox.update_from_path, paths[1:])
        index.insert(len(neighborhoods), list(bbox.get_points()[0])+list(bbox.get_points()[1]))
        neighborhoods.append((entry['properties']['borough'], entry['properties']['neighborhood'], shape(entry['geometry'])))
    neighborhoods.append(('UNKNOWN', 'UNKNOWN', None))    

def locateNeighborhood(location, index, neighborhoods):
    try:
        if(checkLocationValidity(location)):
            point = Point(location[0], location[1])
            match = index.intersection((location[0], location[1], location[0], location[1]))
            for entry in match:
                if neighborhoods[entry][2].contains(point):
                    return entry
        return -1
    except Exception,e:
        print >> sys.stderr, ("Neighborhood Invalid", location, str(e))
        return -1
        
def readInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split(',')
        if len(values) > 1 and values[0] != 'VendorID': 
            yield values

def mapper():
    # Import file as JSON
    with open('pediacitiesnycneighborhoods.geojson') as f:
		js = json.load(f)
	
    neighborhoods = []
    index = rtree.Index()    
    readNeighborhoodData(js['features'], index, neighborhoods)
    
    for values in readInput():
        if(comparePickDropTime(values[1], values[2])):
            pickup_location = (float(values[5]), float(values[6]))
            dropoff_location = (float(values[9]), float(values[10]))
            
            pickup_index = locateNeighborhood(pickup_location, index, neighborhoods)
            dropoff_index = locateNeighborhood(dropoff_location, index, neighborhoods)
            
            print "%s\t%s,%s,%s,%s" % (','.join(values), neighborhoods[pickup_index][0], neighborhoods[pickup_index][1], neighborhoods[dropoff_index][0], neighborhoods[dropoff_index][1])


if __name__=='__main__':
    mapper()