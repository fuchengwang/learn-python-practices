"""
103. Write a Python program to get system command output.
"""

import os


def get_base_name(path):
    return os.path.basename(path)


print(get_base_name('/Users/wyn/Documents/learn-python-practices/mooc/monisen.py'))
