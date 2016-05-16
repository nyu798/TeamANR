#!/usr/bin/env python

import sys

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	line = line.split(",")
	pickup_datetime = line[1]
	day = pickup_datetime.split(" ", 1)
	day_split = day[0].split("-")
	month = day_split[1]
	# Month-wise trips of Manhattan using neighborhood as the key
	if month == "12" and line[19] == "Manhattan" :
		print "%s\t1" % (line[20])