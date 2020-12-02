import random
import pandas as pd
import string
import os
from file_path import locate_file


class Vin:

    FILE_DIR = 'source_data/original_data.csv'

    def __init__(self):
        self.target_file = locate_file(Vin.FILE_DIR)
        self.data = pd.read_csv(self.target_file, header=None)
        self.vins = None
        self.prev_char = None
        self.char_cnt = 0
        self.seq_pttrn = ''
        self.patterns = {}

    def _convert_char(self, char):
        try:
            new_char = int(char)
            return new_char
        except Exception:
            return char

    def _reset(self):
        self.prev_char = None
        self.char_cnt = 0
        self.seq_pttrn = ''

    def _decode_patterns(self):
        # loop through each vin and decode its format
        for vin in self.vins:
            for char in vin:
                # convert a character into a integer otherwise keep it as string
                char = self._convert_char(char)
                if type(char) != type(self.prev_char):
                    if self.prev_char is not None:
                        self.seq_pttrn += '{}-'.format(str(self.char_cnt))
                    self.char_cnt = 0
                    self.prev_char = char
                self.char_cnt += 1
            self.seq_pttrn += '{}'.format(str(self.char_cnt))
            self.patterns[self.seq_pttrn] = self.patterns.get(
                self.seq_pttrn, 0) + 1
            # reset meta data to decode next vin
            self._reset()
        return self.patterns

    def _generate_substr(self, n, char_type):
        if char_type == 's':
            alphabet = string.ascii_uppercase
            sub_str = ''
            for _ in range(n):
                char = random.choice(alphabet)
                sub_str += char
        elif char_type == 'i':
            sub_str = ''
            for _ in range(n):
                sub_str += str(random.randint(0, 9))
        return sub_str

    def _trace_vins(self):
        vins_df = self.data.iloc[:, 2:3]
        self.vins = list(map(lambda x: x[0], vins_df.values))
        return self.vins

    def _generator_vin_format(self):
        self.vins = self._trace_vins()
        self.patterns = self._decode_patterns()
        vin_formations = self.patterns.keys()
        target_vin_formation = random.choice(vin_formations)
        return target_vin_formation

    def generate_vin(self):
        pattern = self._generator_vin_format()
        tokens = pattern.split('-')
        new_vin = ''
        for i, token in enumerate(tokens):
            num = int(token)
            if i % 2 == 0:
                char_type = 's'
            else:
                char_type = 'i'
            new_vin += self._generate_substr(num, char_type)
        return new_vin


def main():
    vin = Vin()
    print(vin.generate_vin())


if __name__ == '__main__':
    main()
