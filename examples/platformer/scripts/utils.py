import os

def get_relative_path(path):
    return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), path))
