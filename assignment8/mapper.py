#!/usr/bin/python

import sys

for line in sys.stdin:
  	data = line.strip().split(" ")
    	if len(data) !=10:
		continue 
	path= data[6]
	filename = path.strip().split("/")[-1:]
		print "{0}\t{1}".format(filename, path)
	
