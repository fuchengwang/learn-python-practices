#_*_ coding:utf-8 _*_ 

"""
46. Write a python program to get the path and name of the file that is currently executing. 
"""

import os

print(os.path.realpath(__file__))   
print(os.path.abspath(__file__))  # 消除符号链接, 得到最原始的地址
