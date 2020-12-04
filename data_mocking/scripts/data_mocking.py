import argparse
from vin_gen import Vin
from incident_gen import IncidentType
from vehicle_gen import Vehicle
from file_path import locate_file
import pandas as pd
import random


class PostSalesReport:
    """
    To generate raw data based on original dataset
    """

    def __init__(self):
        """
        Instantiate vin class, incident class, vehicle class 
        and set path for the output file.
        """
        self.vin = Vin()
        self.incident = IncidentType()
        self.vehicle = Vehicle()
        self.dstn = locate_file('source_data/data.csv')

    def _generate_records(self):
        """
        Generate instances for a single vehicle identified by its VIN.
        Instances per VIN is limited to 10. 
        The first instance is always 'I', which means initial sale.
        Instances 'A' (accidents) and 'R' (repairs) make up the rest of the instances per vin 
        determined by random number.

        Returns
        ----------
        str: all records per VIN concatenated
        """
        # limit number of instances per vehicle to 10
        instances_per_vin = random.randint(2, 10)

        # the number of 'A' and 'R' incidents combined is equal to
        # the number of instances per VIN minus one initial sale instance of that VIN
        incidents_per_vin = instances_per_vin - 1

        new_records = ''
        # initial sale of a vehicle
        inc = self.incident.generate_incident(initial_sale=True)
        vin = self.vin.generate_vin()
        veh = self.vehicle.generate_vehicle_info()
        new_records += self._format_record(inc, vin, veh, initial_sale=True)

        # once intial sale and vehicle vin and make, model, year are generated,
        # the rest of instances are made up of random number of accidents and repairs
        while incidents_per_vin > 0:
            inc = self.incident.generate_incident()
            new_records += self._format_record(inc, vin, veh)
            incidents_per_vin -= 1

        return new_records

    def _format_record(self, incident, vin, vehicle, initial_sale=False):
        """
        Concatenate generated vehicle information.

        Parameters
        ----------
        incident: str, randomly generated incident

        vin: str, randomly generated VIN

        vehicle: str, randomly generated vehicle information

        initial_sale: bool, optional, True or False, if True returns 'I' as default incident

        Returns
        ----------
        str: one instance per vin
        """
        if initial_sale:
            return "{},{},{},,\n".format(incident, vin, vehicle)
        return "{},{},,,,,\n".format(incident, vin)

    def generate_data(self, num):
        """
        Write new records to file. Allow user specified number of vehicles.

        Parameters
        ----------
        num: int, numbers of unique VINs to produce, user defined
        """
        with open(self.dstn, 'w') as f:
            for _ in range(num):
                line = self._generate_records()
                f.write(line)


def parse_args():
    """
    Allow user to set the number of unique vehicles.
    """
    parser = argparse.ArgumentParser(
        prog="Post_Sale_Automobile_Analysis")
    parser.add_argument('--gen_n', type=int, default=500,
                        help='generate n unique vehicle vins')
    return parser.parse_args()


def main():
    args = parse_args()
    num_vins = args.gen_n
    psr = PostSalesReport()
    psr.generate_data(num_vins)


if __name__ == '__main__':
    main()
