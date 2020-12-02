import os


def locate_file(file_in_root_path):
    cur_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    proj_root_path, _ = os.path.split(cur_file_path)
    target_file_path = os.path.join(proj_root_path, file_in_root_path)
    return target_file_path
