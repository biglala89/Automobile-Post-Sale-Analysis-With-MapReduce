
import random


class IncidentType:
    def __init__(self):
        self.initial_sale = 'I'
        self.other_incidents = ('A', 'R')

    def generate_incident(self, initial_sale=False):
        if initial_sale:
            return 'I'
        return random.choice(self.other_incidents)


def main():
    incident = IncidentType()
    incidnet_list = [incident.generate_incident() for _ in range(5)]
    print(incidnet_list)


if __name__ == '__main__':
    main()
