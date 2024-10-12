#!/usr/bin/env python

import sys
import re

# def main(argv):
#     line = sys.stdin.readline()
#     pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
#     try:
#         while line:
#             for word in pattern.findall(line):
#                 print ("LongValueSum:" + word.lower() + "\t" + "1")
#                 # x = 1 / random.randint(0,99)
#             line = sys.stdin.readline()
#     except EOFError as error:
#         return None

# if __name__ == "__main__":
#     main(sys.argv)

def main(argv):
    line = sys.stdin.readline()
    pattern = re.compile(r'\"(\w+)\s')
    try:
        for line in sys.stdin:
            match = pattern.search(line)
            if match:
                method = match.group(1)  # Extract the request method (e.g., GET, POST)
                print(f"{method}\t1")
                

    except EOFError as error:
        return None


if __name__ == "__main__":
    main(sys.argv)