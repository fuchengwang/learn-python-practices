"""
81. Write a Python program to concatenate N strings.
"""


def concat(*strings):
    return ''.join(strings)


print(concat('hello', ' ', 'world', '!'))
