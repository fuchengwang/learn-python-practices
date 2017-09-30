#_*_ coding: utf-8 _*_
"""

47. Write a Python program to find out the number of CPUs using.
"""

import os
import multiprocessing

print(multiprocessing.cpu_count())
# print(os.cpu_count())  # 仅适用于 python3