#!/usr/bin/env python

import sys
import json
import datetime
from rtree import index as rtree
from shapely.geometry import Point, shape
import matplotlib
from matplotlib.path import Path
import numpy
import urllib2

sys.path.append('.')

# Filtering by checking the validity of the location
def checkLocationValidity(location):
	try:
		if(location[0] != 0 and location[1] != 0):
			return True
		else:
			return False
	except:
		return False
		
# Check the validity of pickup and dropoff time
def comparePickDropTime(pickup_value, dropoff_value):
	try:
		pickup_date, pickup_time = pickup_value.split(' ')
		pickup_yr, pickup_mth, pickup_day = pickup_date.split('-')
		pickup_hrs, pickup_mins, pickup_secs = pickup_time.split(':')
		
		dropoff_date, dropoff_time = dropoff_value.split(' ')
		dropoff_yr, dropoff_mth, dropoff_day = dropoff_date.split('-')
		dropoff_hrs, dropoff_mins, dropoff_secs = dropoff_time.split(':')
		
		pickup_yr = int(pickup_yr)
		pickup_mth = int(pickup_mth)
		pickup_day = int(pickup_day)
		pickup_hrs = int(pickup_hrs)
		pickup_mins = int(pickup_mins)
		pickup_secs = int(pickup_secs)
		dropoff_yr = int(dropoff_yr)
		dropoff_mth = int(dropoff_mth)
		dropoff_day = int(dropoff_day)
		dropoff_hrs = int(dropoff_hrs)
		dropoff_mins = int(dropoff_mins)
		dropoff_secs = int(dropoff_secs)
		
		time1 = datetime.datetime(pickup_yr, pickup_mth, pickup_day, pickup_hrs, pickup_mins, pickup_secs)
		time2 = datetime.datetime(dropoff_yr, dropoff_mth, dropoff_day, dropoff_hrs, dropoff_mins, dropoff_secs)
		
		return time1 < time2
	except:
		return False

def locateNeighborhood(index, location, areas):
	try:
		if(checkLocationValidity(location)):
			point = Point(location[0], location[1])
			match = index.intersection((location[0], location[1], location[0], location[1]))
			for entry in match:
				if areas[entry][2].contains(point):
					return entry
		return -1
	except Exception,e:
		return -1
		
def readInput():
	for line in sys.stdin:
		line = line.strip()
		values = line.split(',')
		if len(values) > 1 and values[0] != 'VendorID': 
			yield values

def mapper():
	# Import file as JSON
	with open('pediacitiesnycneighborhoods.geojson') as f:
		js = json.load(f)
	
	areas = []
	
	index = rtree.Index()
	
	for entry in js['features']:
		paths = map(Path, entry['geometry']['coordinates'])
		bbox = paths[0].get_extents()
		map(bbox.update_from_path, paths[1:])
		size = len(areas)
		index.insert(size, list(bbox.get_points()[0])+list(bbox.get_points()[1]))
		areas.append((entry['properties']['borough'], entry['properties']['neighborhood'], shape(entry['geometry'])))
	areas.append(('UNKNOWN', 'UNKNOWN', None))
	
	for values in readInput():
		if(comparePickDropTime(values[1], values[2])):
			pickup_location = (float(values[5]), float(values[6]))
			dropoff_location = (float(values[9]), float(values[10]))
			
			p_index = locateNeighborhood(index, pickup_location, areas)
			d_index = locateNeighborhood(index, dropoff_location, areas)
			
			print "%s\t%s,%s,%s,%s" % (','.join(values), areas[p_index][0], areas[p_index][1], areas[d_index][0], areas[d_index][1])


if __name__=='__main__':
	mapper()