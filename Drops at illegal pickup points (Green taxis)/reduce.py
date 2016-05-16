#!/usr/bin/env python

import sys

current_neighborhood = None
trips = 0

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	neighborhood, count = line.split("\t", 1)
	
	try:
		count = int(count)
	except ValueError:
		continue
	
	if current_neighborhood == neighborhood :
		trips += count
	else :
		if current_neighborhood :
			print "%s\t%d" % (current_neighborhood, trips)
		current_neighborhood = neighborhood
		trips = count

if current_neighborhood :
	print "%s\t%d" % (current_neighborhood, trips)