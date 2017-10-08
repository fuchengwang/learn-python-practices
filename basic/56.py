# _*_ coding:utf-8 _*_

"""
56. Write a Python program to get height and width of the console window.
"""


import os
# 版本3.3中的新功能。
import cProfile

cProfile.run('os.get_terminal_size()')
