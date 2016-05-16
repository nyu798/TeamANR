#!/usr/bin/env python

import sys

current_neighborhood = None
revenue = 0
trips = 0

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	neighborhood, values = line.split("\t", 1)
	count, total_amount = values.split(",", 1)
	
	try:
		total_amount = float(total_amount)
		count = int(count)
	except ValueError:
		continue
	
	if current_neighborhood == neighborhood :
		revenue += total_amount
		trips += count
	else :
		if current_neighborhood :
			print "%s\t%d\t%.2f" % (current_neighborhood, trips, revenue)
		current_neighborhood = neighborhood
		revenue = total_amount
		trips = 1

if current_neighborhood :
	print "%s\t%d\t%.2f" % (current_neighborhood, trips, revenue)