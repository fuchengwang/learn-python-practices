"""
50. Write a Python program to print without newline or space.
"""

# print('are you ok?', end='')

from sys import stdout

for i in range(10):
    stdout.write('*')