"""
79. Write a Python program to get the size of an object in bytes.
"""

import sys
import string


def test():
    return sys.getsizeof(dict(zip(string.ascii_lowercase, [0]*26)))


print(test())
