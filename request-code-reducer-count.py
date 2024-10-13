#!/usr/bin/env python

'''request-code-reducer-count.py'''
import sys

request_count = {}


for line in sys.stdin:
    code, count = line.strip().split('\t', 1)
    try:
        count  = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if code not in request_count:
        request_count[code] = 0

    request_count[code] += count

for code, count in request_count.items():
    print(f"{code}\t{count}")
