#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) != 10:
		continue
	dateItem = data[3]
	
	date = dateItem.strip().split("/")[2]
	year= date.strip().split(":")[0]
	if year == '2009' or year == '2010' or year == '2011':
		print year

    	


