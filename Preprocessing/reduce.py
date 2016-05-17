#!/usr/bin/env python

import sys

def readInput():
	for line in sys.stdin:
		line = line.strip()
		yield line.split('\t')

def reducer():
	for key, value in readInput():
		print '%s,%s' % (key, value)

if __name__=='__main__':
	reducer()