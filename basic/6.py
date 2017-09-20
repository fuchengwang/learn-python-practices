# _*_ coding: utf-8 _*_

"""
6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 

Sample data : 3, 5, 7, 23
Output : 
List : ['3', ' 5', ' 7', ' 23'] 
Tuple : ('3', ' 5', ' 7', ' 23')
"""


str = raw_input("input a sequence of comma-separated numbers:")

lst = str.split(',')
print lst
print tuple(lst)



