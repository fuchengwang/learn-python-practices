"""
Write a Python program to check if a string is numeric.
"""


def is_numeric(str):
    try:
        float(str)
        return True
    except ValueError as e:
        return False


print(is_numeric('18'))
