#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:57:25 2017

@author: wyn

68. Write a Python program to calculate the sum of the digits in an integer.
"""

import functools

def digits_sum(num):
    return functools.reduce(lambda x, y: int(x) + int(y), str(num))
    # return sum(int(i) for i in str(num))




print(digits_sum(123456789))

