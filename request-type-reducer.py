#!/usr/bin/env python

import sys

request_count = {}

total_reqs = 0
for line in sys.stdin:
    total_reqs += 1
    method, count = line.strip().split('\t', 1)
    try:
        count  = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if method not in request_count.keys():
        request_count[method] = count
    else:
        request_count[method] += int(count)

for method, count in request_count.items():
    percentage_of_reqs = (count / total_reqs) * 100
    print(f"{method}\t{percentage_of_reqs:.2f}%")


#     #!/usr/bin/env python
# """reducer.py"""

# from operator import itemgetter
# import sys

# current_word = None
# current_count = 0
# word = None

# # input comes from STDIN
# for line in sys.stdin:
#     # remove leading and trailing whitespace
#     line = line.strip()

#     # parse the input we got from mapper.py
#     word, count = line.split('\t', 1)

#     # convert count (currently a string) to int
#     try:
#         count = int(count)
#     except ValueError:
#         # count was not a number, so silently
#         # ignore/discard this line
#         continue
#     # this IF-switch only works because Hadoop sorts map output
#     # by key (here: word) before it is passed to the reducer
#     if current_word == word:
#         current_count += count
#     else:
#         if current_word:
#             # write result to STDOUT
#             print ('%s\t%s' % (current_word, current_count))
#         current_count = count
#         current_word = word

# # do not forget to output the last word if needed!
# if current_word == word:
#     print ('%s\t%s' % (current_word, current_count))