"""
52. Write a Python program to print to stderr.
"""

import os
import sys

sys.stderr.write('error!\n')


print('err', 'world', file=sys.stderr, sep='__')