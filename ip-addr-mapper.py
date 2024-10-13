#!/usr/bin/env python
'''id-addr-mapper.py'''
import sys
import re


def main(argv):
    line = sys.stdin.readline()
    pattern = re.compile(r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) .*" [4][0-9][0-9] ')
    try:
        while line:
            match = pattern.findall(line)
            if match:
                ip = match[0] # Extract the request method (e.g., GET, POST, HEAD)
                print(f"{ip}\t1")
            line = sys.stdin.readline()
                
    except EOFError as error:
        return None


if __name__ == "__main__":
    main(sys.argv)