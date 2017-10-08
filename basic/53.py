#_*_ coding:utf-8 _*_
"""
53. Write a python program to access environment variables.
"""

import sys


# 模块的搜索路径, 并不是系统环境变量
print(sys.path)  

# os 模块可以访问系统环境变量, 文件描述, 进程信息等

import os
print(os.environ['PATH'])
print(os.getenv('PATH'))