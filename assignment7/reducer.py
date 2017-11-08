#!/usr/bin/python

import sys

Total = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip()
    if data_mapped == "" or data_mapped is None:
	continue
    thisKey = data_mapped

    if oldKey and oldKey != thisKey:
	print oldKey, "\t", Total
        oldKey = thisKey
	Total = 0

    oldKey = thisKey
    Total= Total + 1

if oldKey != None:
    print oldKey, "\t", Total
