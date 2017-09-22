"""
34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
"""

def my_sum(a, b):
    s = a + b
    return 20 if s in range(15, 21) else s

print my_sum(7, 8)
print my_sum(9, 9)
print my_sum(9, 17)