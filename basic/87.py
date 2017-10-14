"""
87. Write a Python program to get the size of a file.
"""

import os


def get_file_size(path):
    if not os.path.isfile(path):
        raise TypeError('not file')

    return os.path.getsize(path)


print(get_file_size('./README.md'))
print(get_file_size('not exist'))
