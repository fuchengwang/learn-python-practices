"""
41. Write a Python program to check whether a file exists.
"""

import os

def is_file(name):
    print os.path.isfile(name)


is_file('filename.py')