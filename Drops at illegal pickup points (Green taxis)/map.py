#!/usr/bin/env python

import sys

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	line = line.split(",")
	if len(line) < 27:
		line.append("UNKNOWN")
		line.append("UNKNOWN")
	dropoff_borough = line[25]
	dropoff_neighborhood = line[26]
	#Create a list of legal pickup points in Manhattan
	legal_pickup_points = ["Roosevelt Island", "Randall's Island", "Harlem", "Morningside Heights", "East Harlem", "Inwood", "Marble Hill", "Washington Heights"] 
	if ( dropoff_borough == "Manhattan" ) :
		if dropoff_neighborhood not in legal_pickup_points :
			print "%s\t1" % (dropoff_neighborhood)
	if ( dropoff_borough == "Queens" ) :
		if ( (dropoff_neighborhood == "John F. Kennedy International Airport") or (dropoff_neighborhood == "LaGuardia Airport") ) :
			print "%s\t1" % (dropoff_neighborhood)