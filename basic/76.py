"""
76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
"""

import sys

script_name = sys.argv[0]
args = sys.argv[1:]

print(script_name, args)