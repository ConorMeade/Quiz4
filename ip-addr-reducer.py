#!/usr/bin/env python

'''id-addr-reducer-count.py'''
import sys

ip_count = {}


for line in sys.stdin:
    ip, count = line.strip().split('\t', 1)
    try:
        count  = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if ip not in ip_count:
        ip_count[ip] = 0

    ip_count[ip] += count

for ip, count in ip_count.items():
    print(f"{ip}\t{count}")
