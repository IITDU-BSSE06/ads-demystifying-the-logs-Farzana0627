#!/usr/bin/python

import sys
countTotal = 0
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thispath = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", countTotal
        oldKey = thispath;
        countTotal = 0

    oldKey = thispath
    countTotal += 1

if oldKey != None:
    print oldKey, "\t", countTotal


