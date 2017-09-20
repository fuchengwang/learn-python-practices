"""
18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
"""

def thrice_sum(a, b, c):
    sum = a + b + c

    if a == b == c:
       sum *= 3

    return sum 

print thrice_sum(2, 2, 2)
print thrice_sum(1, 2, 3)