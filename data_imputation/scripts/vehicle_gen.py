from file_path import locate_file
import pandas as pd
import os
import random


class Vehicle:

    FILE_DIR = 'data_imputation/data/cars.csv'

    def __init__(self):
        self.target_file = locate_file(Vehicle.FILE_DIR)
        self.data = pd.read_csv(self.target_file, header=None)
        self.data.rename(
            columns={0: 'model', 1: 'make', 2: 'year'}, inplace=True)
        self.length = self.data.shape[0]

    def generate_single_car(self):
        rand_num = random.randint(0, self.length)
        new_car = self.data.iloc[rand_num, :]
        print(new_car)


def main():
    vehicle = Vehicle()
    vehicle.generate_single_car()


if __name__ == "__main__":
    main()
