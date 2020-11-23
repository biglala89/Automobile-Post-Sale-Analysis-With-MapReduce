#! /usr/local/bin/python3.7

import sys

cur_make_year = None
total_num_accdt = 0

for line in sys.stdin:
    line = line.rstrip('\n')[1:-1]
    tokens = line.split("'")
    make_year, num_accdt = tokens[1], int(tokens[-1][2:])

    if cur_make_year != make_year:
        if cur_make_year is not None:
            print(cur_make_year, total_num_accdt)
        total_num_accdt = 0
        cur_make_year = make_year

    total_num_accdt += 1

print(cur_make_year, total_num_accdt)
