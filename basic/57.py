# _*_ coding:utf-8 _*_

"""
57. Write a program to get execution time for a Python method.
"""
from datetime import datetime

def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

# 三种方法  1. time  2.datetime 3.timeit
start_time = datetime.now()

fib(33)

end_time = datetime.now();

delta = end_time-start_time

print(delta)




