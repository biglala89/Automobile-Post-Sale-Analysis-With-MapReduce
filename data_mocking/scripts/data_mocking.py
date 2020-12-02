from vin_gen import Vin
from incident_gen import IncidentType
from vehicle_gen import Vehicle
import random
from file_path import locate_file
import pandas as pd


class PostSalesReport:

    def __init__(self):
        self.vin = Vin()
        self.incident = IncidentType()
        self.vehicle = Vehicle()
        self.dstn = locate_file('source_data/mocking_output.csv')

    def _generate_records(self):
        # limit number of instances per vehicle to 10
        instances_per_vin = random.randint(2, 10)
        # number of 'A' and 'R' incidents combined
        incidents_per_vin = instances_per_vin - 1

        new_records = ''
        # initial sale of a vehicle
        inc = self.incident.generate_incident(initial_sale=True)
        vin = self.vin.generate_vin()
        veh = self.vehicle.generate_vehicle_info()
        new_records += self._format_record(inc, vin, veh, initial_sale=True)

        while incidents_per_vin > 0:
            inc = self.incident.generate_incident()
            new_records += self._format_record(inc, vin, veh)
            incidents_per_vin -= 1

        return new_records

    def _format_record(self, incident, vin, vehicle, initial_sale=False):
        if initial_sale:
            return "{},{},{},,\n".format(incident, vin, vehicle)
        return "{},{},,,\n".format(incident, vin)

    def generate_data(self, num):
        with open(self.dstn, 'w') as f:
            for _ in range(num):
                line = self._generate_records()
                f.write(line)


def main():
    psr = PostSalesReport()
    psr.generate_data(50)


if __name__ == '__main__':
    main()
