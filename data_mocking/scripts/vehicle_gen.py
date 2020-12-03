from file_path import locate_file
import pandas as pd
import os
import random


class Vehicle:
    """
    Randomly generate vehicle information for a unique VIN.
    """

    FILE_DIR = 'data_mocking/data/cars.csv'

    def __init__(self):
        """
        Read base data into buffer.
        """
        self.target_file = locate_file(Vehicle.FILE_DIR)
        self.data = self._read_file(self.target_file)

    def _read_file(self, target_file):
        """
        Read base vehicle information and process raw data.

        Parameters
        ----------
        target_file: str, absolute path of sample data

        Returns
        ----------
        list: a list of strings of preprocessed vehicle information 
        consisting of make, model, year
        """
        with open(target_file, 'r') as f:
            lines = f.readlines()
        vehicle_info = list(map(lambda line: line.rstrip('\n'), lines))
        return vehicle_info

    def generate_vehicle_info(self):
        """
        Randomly generate vehicle records from read raw data.

        Returns
        ----------
        str: vehicle data
        """
        return random.choice(self.data)


def main():
    vehicle = Vehicle()
    for _ in range(10):
        print(vehicle.generate_vehicle_info())


if __name__ == "__main__":
    main()
