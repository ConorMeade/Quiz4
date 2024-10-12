#!/usr/bin/python

import sys

request_count = {}


for line in sys.stdin:
    method, count = line.strip().split('\t')
    request_count[method] += int(count)

total_reqs = sum(request_count.values())

for method, count in request_count.items():
    percentage_of_reqs = (count / total_reqs) * 100
    print(f"{method}\t{percentage_of_reqs:.2f}%")