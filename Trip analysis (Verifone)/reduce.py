#!/usr/bin/python

import sys

current_tip_percentage = None
count = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	line = line.strip()
	line = line.split("\t", 1)
	tip_percentage = line[0]
	
	if current_tip_percentage == tip_percentage :
		count += 1
	else:
		if current_tip_percentage:
			print "%s,%d" % (current_tip_percentage, count)
		current_tip_percentage = tip_percentage
		count = 1
		
if current_tip_percentage:
	print "%s,%d" % (current_tip_percentage, count)