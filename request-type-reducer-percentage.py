#!/usr/bin/env python

'''reducer_percentage.py'''
import sys

request_percentages = {}
total_requests = 0

for line in sys.stdin:
    request_type, count = line.strip().split('\t')
    count = int(count)
    request_percentages[request_type] = count
    total_requests += count

for request_type, count in request_percentages.items():
    percentage = (count / total_requests) * 100
    print(f"{request_type}\t{count}\t{percentage:.2f}%")