#!/usr/bin/env python

import sys

extra_revenue = 0

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	line = line.split("\t", 1)
	
	extra_revenue_per_trip = line[1]

	try:
		extra_revenue_per_trip = float(extra_revenue_per_trip)
	except ValueError:
		continue
		
	extra_revenue += extra_revenue_per_trip

print "CMT\t%.2f" % (extra_revenue)
