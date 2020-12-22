#! /usr/local/bin/python3.7

import sys

for line in sys.stdin:
    line = line.rstrip('\n')[1:-1]
    tokens = line.split("'")
    make, year, num_accdt = tokens[1], tokens[3], int(tokens[-1][2:])
    make_year_concat = '{} {}'.format(make, year)
    print(make_year_concat, num_accdt)
