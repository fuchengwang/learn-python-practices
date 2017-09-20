# _*_ coding: utf-8 _*_
"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
Sample value of n is 5 
Expected Result : 615
"""

str = raw_input("input an integer: ")
n = int(str)
nn = int(str*2)
nnn = int(str*3)
print n + nn + nnn