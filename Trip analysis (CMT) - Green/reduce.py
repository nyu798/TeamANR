#!/usr/bin/env python

import sys

current_tip_percentage = None
sum = 0

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()

	tip_percentage, count = line.split("\t", 1)

	try:
		count = int(count)
	except ValueError:
		continue

	if current_tip_percentage == tip_percentage :
		sum += count
	else :
		if current_tip_percentage :
			print "%s\t%d" % (current_tip_percentage, sum)
		current_tip_percentage = tip_percentage
		sum = count

if current_tip_percentage :
	print "%s\t%d" % (current_tip_percentage, sum)