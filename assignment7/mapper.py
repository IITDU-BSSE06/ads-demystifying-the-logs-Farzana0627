#!/usr/bin/python

import sys

for line in sys.stdin:
  	data = line.strip().split(" ")
    	if len(data) !=10:
		continue
	http= "HTTP"
	HTTPexists= http in line 
	
	if HTTPexists:
		print data[5][1:] 
		
