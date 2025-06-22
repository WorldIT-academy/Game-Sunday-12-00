import os

def find_path(name: str):
    path = os.path.join(__file__, "..", "..", name)
    path = os.path.abspath(path)
    return path