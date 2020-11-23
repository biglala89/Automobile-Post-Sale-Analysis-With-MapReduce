#! /usr/local/bin/python3.7

import sys

group_level_master_info = {}
vehicle_accidents = {}

for line in sys.stdin:
    vin, info = line.split('\t')
    info = info.rstrip('\n')
    accident_type = info[2]
    make = info[7:-10]
    year = info[-6:-2]

    if accident_type == 'I':
        group_level_master_info[vin] = (accident_type, make, year)

    if accident_type == 'A':
        vehicle_accidents[vin] = vehicle_accidents.get(vin, 0) + 1

for vin, num_accdt in vehicle_accidents.items():
    make, year = group_level_master_info[vin][1], group_level_master_info[vin][2]
    for _ in range(num_accdt):
        print(make, year, 1)
