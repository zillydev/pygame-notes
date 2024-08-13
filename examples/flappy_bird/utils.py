import os

def get_relative_path(path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
