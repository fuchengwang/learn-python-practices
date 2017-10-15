"""
1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
"""

import re
import string


def is_specific_char(str):
    matched = re.search(r'^[0-9a-zA-Z]+$', str)
    print(matched is not None)


def is_specific_char2(str):
    matched = re.search(r'[^0-9a-zA-Z]', str)
    print(matched is None)


is_specific_char(string.ascii_letters+string.digits)  # True
is_specific_char(string.printable)  # False

is_specific_char2(string.ascii_letters+string.digits)  # True
is_specific_char2(string.printable)  # False
