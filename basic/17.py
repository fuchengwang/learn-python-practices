# _*_ coding: utf-8 _*_

"""
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

# 题意为 与1000或2000差值在100之内(包括100)

num = int(raw_input("input a number: "))

if (abs(num-1000) <= 100 or abs(num-2000) <= 100):
    print True
else:
    print False


