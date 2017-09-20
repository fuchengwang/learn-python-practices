"""
16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
"""

num = int(raw_input("Enter number: "))
diff = abs(num - 17)

if num > 17:
    print diff * 2
else:
    print diff

