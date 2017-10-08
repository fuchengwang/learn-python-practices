#_*_ coding:utf-8 _*_

"""
51. Write a Python program to determine profiling of Python programs.

Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module. 
"""

## 测试程序开销

import cProfile
import re

def sum(a, b):
    return ''.join([a, b])

# 1 1 2 3 5 8
def fib(n):
    if n < 2:
        return 1

    return fib(n-1) + fib(n-2)


pr = cProfile.Profile()
pr.enable()

m = fib(34)
print(m)


pr.disable()
pr.print_stats()


