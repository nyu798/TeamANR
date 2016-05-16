#!/usr/bin/env python

import sys

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	line = line.split(",")
	if len(line) < 27:
		line.append("UNKNOWN")
		line.append("UNKNOWN")
	trip_type = line[20]
	pickup_borough =  line[23]
	pickup_neighborhood = line[24]
	try:
		total_amount = float(line[18])
	except ValueError:
		continue
	#Create a list of legal pickup points in Manhattan
	legal_pickup_points = ["Roosevelt Island", "Randall's Island", "Harlem", "Morningside Heights", "East Harlem", "Inwood", "Marble Hill", "Washington Heights"] 
	if ( pickup_borough == "Manhattan" ) :
		if pickup_neighborhood not in legal_pickup_points :
			print "%s\t1,%.2f" % (pickup_neighborhood, total_amount)
	if ( pickup_borough == "Queens" ) :
		if ( (pickup_neighborhood == "John F. Kennedy International Airport" and trip_type != "2") or (pickup_neighborhood == "LaGuardia Airport" and trip_type != "2") ) :
			print "%s\t1,%.2f" % (pickup_neighborhood, total_amount)
		