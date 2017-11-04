#!/usr/bin/python

import sys

Total = 0

for line in sys.stdin:
    data = line.strip()
    if data == "/assets/js/the-associates.js":
	 Total=Total+1
	
print  Total
