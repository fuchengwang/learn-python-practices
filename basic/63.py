# -*- utf-8 -*-


"""
write a Python program to get an absolute file path.
"""

import os

def get_abs_path(path):
    return os.path.abspath(path)


print(get_abs_path('monisen.py'))