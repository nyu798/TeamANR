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
		#Check if vendor is CMT and whether payment is by credit card
		if line[0] == "1" and line[11] == "1" :
			fare_amount = line[12]
			surcharge = line[13]
			mta_tax = line[14]
			tip_amount = line[15]
			tolls_amount = line[16]
			try:
				fare_amount = float(fare_amount)
				surcharge = float(surcharge)
				mta_tax = float(mta_tax)
				tip_amount = float(tip_amount)
				tolls_amount = float(tolls_amount)
			except ValueError:
				continue
			#Check the validity of data	
			if fare_amount + surcharge + mta_tax + tolls_amount > 0 and tip_amount < fare_amount + surcharge + mta_tax + tolls_amount:
				tip_percentage = (tip_amount / (fare_amount + surcharge + mta_tax + tolls_amount)) * 100
				tip_amount2 = tip_percentage/100*(fare_amount + surcharge)
				print "CMT\t%.2f" % (tip_amount - tip_amount2)
