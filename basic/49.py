"""
49. Write a Python program to list all files in a directory in Python. 
"""

import os

d = os.getcwd()
for i in os.listdir(d):
    print(i)


'python3 scandir yield DirEntry objects'
files = [i.name for i in os.scandir() if i.is_file()]

print(files)