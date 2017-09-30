"""
48. Write a Python program to parse a string to Float or Integer. 
"""

def str2number(str):
    number = eval(str)
    print(number, type(number))
    
str2number("3.14")
str2number("5")
