#!/usr/bin/python

import sys
import math

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	if "VendorID" not in line:
		if not line.strip():
			continue
		line = line.strip()
		line = line.split(",")
		#Check if vendor is Verifone and whether payment is by credit card
		if line[0] == "2" and line[19] == "1" :
			fare_amount = line[11]
			surcharge = line[12]
			tip_amount = line[14]
			try:
				fare_amount = float(fare_amount)
				surcharge = float(surcharge)
				tip_amount = float(tip_amount)
			except ValueError:
				continue
			#Check the validity of data 
			if fare_amount + surcharge > 0 and tip_amount < fare_amount + surcharge :
				#Calculate tip percentage
				tip_percentage = (tip_amount / (fare_amount + surcharge)) * 100
				floor_tip_percentage = math.floor(tip_percentage)
				ceil_tip_percentage = math.ceil(tip_percentage)
				if (tip_percentage - floor_tip_percentage) < (ceil_tip_percentage - tip_percentage) :
					tip_percentage = floor_tip_percentage
				else:
					tip_percentage = ceil_tip_percentage
				tip_percentage = int(tip_percentage)
				print "%d\t1" % (tip_percentage)
	