# check.py

import os

def isfile(path):
    """
    verifica se path é file
    """
    isfile = os.path.isfile(path)
    return isfile

def isfolder(path):
    """
    verifica se path é folder
    """
    isfolder = os.path.isdir(path)
    return isfolder
