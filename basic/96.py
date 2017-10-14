"""
96. Write a Python program to print the current call stack.
"""

import traceback


def func2():
    traceback.print_stack()

def func1():
    func2()

def func0():
    func1()

func0()
