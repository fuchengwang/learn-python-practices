"""
70. Write a Python program to sort files by date. 
"""

import os

def show_files_by_date(dir):
    entrys = os.scandir(dir)  

    entrys = sorted(entrys, key=lambda e: e.stat().st_ctime)  
    for entry in entrys:
        print(entry.name)


show_files_by_date('basic/')

