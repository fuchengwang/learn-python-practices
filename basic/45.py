"""
Write a python program to call an external command in Python.
"""

# cmd = raw_input("input the command: ")

import subprocess

subprocess.call('ls -l', shell=True)