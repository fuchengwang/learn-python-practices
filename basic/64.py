#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:20:53 2017

@author: wyn

64. Write a Python program to get file creation and modification date/times.
"""

import os
from datetime import datetime

filename = '63.py'
stat = os.stat(filename)
d = datetime.fromtimestamp(stat.st_ctime)
print(d)