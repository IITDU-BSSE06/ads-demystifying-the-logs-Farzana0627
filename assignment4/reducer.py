#!/usr/bin/python

import sys

Total = 0
oldKey = None
Max=0

for line in sys.stdin:
    data_mapped = line.strip()
    if data_mapped == "" or data_mapped is None:
	continue
    thisKey = data_mapped

    if oldKey and oldKey != thisKey:
        if Total>Max:
		Max= Total
		maxhitpath= oldKey
        oldKey = thisKey;
        Total = 0

    oldKey = thisKey
    Total = Total+1

print maxhitpath, "\t", Max, " times" 
