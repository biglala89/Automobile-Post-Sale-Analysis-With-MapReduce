import random
import pandas as pd
import string
import os
from file_path import locate_file


class Vin:
    """
    Randomly generate unique vehicle VIN.
    """

    FILE_DIR = 'source_data/sample_data.csv'

    def __init__(self):
        """
        Locate source data and read it into memory.
        Set meta data for decoding VINs' patterns.
        Initialize a dictionary to record each VIN's pattern.
        """
        self.target_file = locate_file(Vin.FILE_DIR)
        self.data = pd.read_csv(self.target_file, header=None)
        self.vins = None
        self.prev_char = None
        self.char_cnt = 0
        self.seq_pttrn = ''
        self.patterns = {}

    def _convert_char(self, char):
        """
        Convert human-read integer character from VIN string to integer, 
        keep as-is if conversion raises error.

        Parameters
        ----------
        char: str, type of a character from a string

        Returns
        ----------
        int or str: 
            For example, int('3') --> 3, int('s') --> raise error, keep it as 's'
        """
        try:
            new_char = int(char)
            return new_char
        except Exception:
            return char

    def _reset(self):
        """
        Reset meta data to initial state.
        """
        self.prev_char = None
        self.char_cnt = 0
        self.seq_pttrn = ''

    def _decode_patterns(self):
        """
        Loop over each vin and decode its format.

        Returns
        ----------
        str: VIN's format. Each number represents a succession of strings or integers
            for example, '3-6-2-5' means 3 strings + 6 integers + 2 strings + 5 integers
        """
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
        """
        Generate a section of a randomly chosen VIN.

        Parameters
        ----------
        n: int, integer from VIN's format string (3 in '3-6-2-5')

        char_type: str, string type of a character, 's' means string, 'i' means integer

        Returns
        ----------
        str: a section of string
        """
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
        """
        Select column containing the VINs from the original dataset.

        Returns
        ----------
        list: a list of strings of VINs from the original dataset
        """
        vins_df = self.data.iloc[:, 2:3]
        self.vins = list(map(lambda x: x[0], vins_df.values))
        return self.vins

    def _generator_vin_format(self):
        """
        Randomly generate a VIN format from a pool of available decoded 
        sample VINs' formats.

        Returns
        ----------
        str: a format of VIN (i.e. '4-5-3-4')
        """
        self.vins = self._trace_vins()
        self.patterns = self._decode_patterns()
        vin_formations = self.patterns.keys()
        target_vin_formation = random.choice(vin_formations)
        return target_vin_formation

    def generate_vin(self):
        """
        Generate a new VIN.

        Returns
        ----------
        str: a randomly generated new VIN
            for example, 'BPUX42819ZQ028411'
        """
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
