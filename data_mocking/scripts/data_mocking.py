from vin_gen import Vin
from incident_gen import IncidentType
from vehicle_gen import Vehicle
import random
from file_path import locate_file


class PostSalesReport:

    def __init__(self):
        self.vin = Vin()
        self.incident = IncidentType()
        self.vehicle = Vehicle()
        self.dstn = locate_file('data_imputation/data/output.csv')

    def _generate_records(self):
        random_vin = self.vin.generate_vin()
        random_inc = self.incident.generate_incident()
        random_veh = self.vehicle.generate_vehicle_info()
        return random_vin, random_inc, random_veh

    def generate_file(self, num):
        with open(self.dstn, 'w') as f:
            for _ in range(num):
                vin, inc, veh = self._generate_records()
                f.write('{},{},{}\n'.format(vin, inc, veh))


def main():
    psr = PostSalesReport()
    psr.generate_file(100)


if __name__ == '__main__':
    main()
