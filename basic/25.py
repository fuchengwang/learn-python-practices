"""
25. Write a Python program to check whether a specified value is contained in a group of values. 
Test Data : 
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""

def is_group_member(lst, value):
    return value in lst

print in_group([1, 5, 8, 3], 3)
print in_group([1, 5, 8, 3], -1)