"""
59. Write a Python program to convert height (in feet and inches) to centimeters.

1feet = 12inch
1inch = 2.54cm
"""

def convert_to_cm(feet=0, inch=0):
    inch += feet * 12
    return round(inch * 2.54, 0)


print "%d" % convert_to_cm(5, 3)
