#!/usr/bin/python

import sys

Total = 0

for line in sys.stdin:
    data = line.strip()
    if data == "":
	continue
    if data == "10.99.99.186":
	 Total=Total+1
	
print  Total
