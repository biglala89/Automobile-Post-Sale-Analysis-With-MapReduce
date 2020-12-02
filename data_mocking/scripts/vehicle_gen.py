from file_path import locate_file
import pandas as pd
import os
import random


class Vehicle:

    FILE_DIR = 'data_imputation/data/cars.csv'

    def __init__(self):
        self.target_file = locate_file(Vehicle.FILE_DIR)
        self.data = self._read_file(self.target_file)

    def _read_file(self, target_file):
        with open(target_file, 'r') as f:
            lines = f.readlines()
        vehicle_info = list(map(lambda line: line.rstrip('\n'), lines))
        return vehicle_info

    def generate_vehicle_info(self):
        return random.choice(self.data)


def main():
    vehicle = Vehicle()
    for _ in range(10):
        print(vehicle.generate_vehicle_info())


if __name__ == "__main__":
    main()
