#!/usr/bin/python

import sys

Total = 1
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip()
    if data_mapped == "" or data_mapped is None:
	      continue
    thisKey = data_mapped

    if oldKey and oldKey != thisKey:
	      Total= Total+1
        oldKey = thisKey;

    oldKey = thisKey

print Total, " unique files." 
