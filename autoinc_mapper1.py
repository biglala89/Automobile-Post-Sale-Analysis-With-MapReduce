#! /usr/local/bin/python3.7

import sys

for line in sys.stdin:
    tokens = line.split(',')
    key, value = tokens[2], (tokens[1], tokens[3], tokens[5])
    print('{}\t{}'.format(key, value))
