#!/usr/bin/python

import sys

countTotal = 0
oldKey = None
maximum = 0
maxKey = None

for line in sys.stdin:
     data = line.strip()
     if data == "" or data is None:
             continue
     thisKey = data
     if oldKey and oldKey != thisKey:
             if maximum < countTotal:
                     maximum = countTotal
                     maxKey = oldKey
             print oldKey, "\t", countTotal
             oldKey = thisKey
             countTotal = 0
     oldKey = thisKey
     countTotal = countTotal + 1

if oldKey != None:
    print oldKey, "\t", countTotal
if maximum < countTotal:
                     maximum = countTotal
                     maxKey = oldKey

print maxKey," has maximum hits of ",  maximum, " times."


