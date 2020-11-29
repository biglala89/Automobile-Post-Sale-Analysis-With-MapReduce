import os


def locate_file(filedir):
    cur_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dirname, _ = os.path.split(cur_file)
    target_file = os.path.join(dirname, filedir)
    return target_file
