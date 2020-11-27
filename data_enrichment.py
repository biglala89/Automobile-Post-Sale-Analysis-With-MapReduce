import random
import pandas as pd


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
            try:
                new_char = str(char)
                return new_char
            except Exception as e:
                raise e

    def _reset(self):
        self.prev_char = None
        self.char_cnt = 0
        self.seq_pttrn = ''

    def find_pattens(self):
        self._reset()

        for vin in self.vins:
            print(vin)
            for char in vin:
                char = self._convert_char(char)
                if type(char) != type(self.prev_char):
                    if self.prev_char is not None:
                        self.seq_pttrn += '{}-'.format(str(self.char_cnt))
                    self.char_cnt = 0
                    self.prev_char = char
                self.char_cnt += 1
            self.seq_pttrn += '{}'.format(str(self.char_cnt))
            print(self.seq_pttrn)
            self.patterns[self.seq_pttrn] = self.patterns.get(
                self.seq_pttrn, 0) + 1

            self._reset()
        print(self.seq_pttrn)
        print(self.patterns)

    def generate(self):
        pass


def main():
    dataset = Dataset()
    vins_df = dataset.data.iloc[:, 2:3]
    vin_strings = list(map(lambda x: x[0], vins_df.values))
    vin = Vin(vin_strings)
    vin.find_pattens()


if __name__ == '__main__':
    main()
