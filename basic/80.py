"""
80. Write a Python program to get the current value of the recursion limit.
"""

import sys


print(sys.getrecursionlimit())

sys.setrecursionlimit(800)

print(sys.getrecursionlimit())
