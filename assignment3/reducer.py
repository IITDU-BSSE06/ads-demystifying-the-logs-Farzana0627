#!/usr/bin/python

import sys

Total = 0
oldKey = None
Max = 0
maxhitpath = None

for line in sys.stdin:
    data_mapped = line.strip()
    thisKey = data_mapped

    if oldKey and oldKey != thisKey:
        if Total>Max:
		        Max = Total
		        maxhitpath = oldKey
        oldKey = thisKey;
        Total = 0

    oldKey = thisKey
    Total = Total+1

print maxhitpath
