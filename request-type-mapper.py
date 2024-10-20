#!/usr/bin/env python


'''request-type-mapper.py'''
import sys
import re


def main(argv):
    line = sys.stdin.readline()
    pattern = re.compile(r'\"(\w+)\s')
    try:
        while line:
            match = pattern.findall(line)
            if match:
                method = match[0] # Extract the request method (e.g., GET, POST, HEAD)
                print(f"LongValueSum:{method}\t1")
            line = sys.stdin.readline()
                
    except EOFError as error:
        return None


if __name__ == "__main__":
    main(sys.argv)