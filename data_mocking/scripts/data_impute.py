from vin_gen import Vin
from incident_gen import IncidentType
from vehicle_gen import Vehicle
import random


class PostSalesReport:

    def __init__(self):
        self.vin = Vin()
        self.incident = IncidentType()
        self.vehicle = Vehicle()

    def generate_records(self, n):
        for _ in range(n):
            print(self.vin.generate_vin())
            print(self.incident.generate_incident())
            print(self.vehicle.generate_vehicle_info())
            print('-'*30)


def main():
    psr = PostSalesReport()
    psr.generate_records(10)


if __name__ == '__main__':
    main()
