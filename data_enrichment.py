import random
import pandas as pd
import string


class Dataset:

    FILE = './data/original_data.csv'

    def __init__(self):
        self.data = pd.read_csv(Dataset.FILE, header=None)
        self.dimension = self.data.shape


class Vin:
    def __init__(self, vins):
        self.vins = vins
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

    def decode_patterns(self):
        self._reset()

        # loop through each vin and decode its format
        for vin in self.vins:
            for char in vin:
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

    def generate_single_vin(self, pattern):
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
    dataset = Dataset()
    vins_df = dataset.data.iloc[:, 2:3]
    vin_strings = list(map(lambda x: x[0], vins_df.values))
    vin = Vin(vin_strings)
    vin_patterns = vin.decode_patterns()
    vin_pools = vin_patterns.keys()
    target_vin_pattern = random.choice(vin_pools)
    print(vin.generate_single_vin(target_vin_pattern))


if __name__ == '__main__':
    main()
