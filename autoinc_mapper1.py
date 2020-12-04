#! /usr/local/bin/python3.7

import sys

for line in sys.stdin:
    tokens = line.split(',')
    key, value = tokens[1], (tokens[0], tokens[2], tokens[4])
    print('{}\t{}'.format(key, value))
