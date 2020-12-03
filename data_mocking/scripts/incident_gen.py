import random


class IncidentType:
    """
    Randomly generate incidents for a unique VIN.
    """

    def __init__(self):
        self.initial_sale = 'I'
        self.other_incidents = ('A', 'R')

    def generate_incident(self, initial_sale=False):
        """
        The first incident is always initial sale.
        The number of 'A's and 'R's is randomly generated.

        Parameters
        ----------
        initial_sale: bool, optional, True or False, if True returns 'I' as default incident

        Returns
        ----------
        str: randomly chosen incident type, except the first one for each VIN
        """
        if initial_sale:
            return 'I'
        return random.choice(self.other_incidents)


def main():
    incident = IncidentType()
    incidnet_list = [incident.generate_incident() for _ in range(5)]
    print(incidnet_list)


if __name__ == '__main__':
    main()
