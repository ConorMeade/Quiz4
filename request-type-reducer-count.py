#!/usr/bin/env python

'''reducer_count.py'''
import sys

request_count = {}


for line in sys.stdin:
    method, count = line.strip().split('\t', 1)
    try:
        count  = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if method not in request_count:
        request_count[method] = 0

    request_count[method] += count

for method, count in request_count.items():
    print(f"{method}\t{count}%")
