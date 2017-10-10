"""
60. Write a Python program to calculate the hypotenuse of a right angled triangle.
"""

def hypotenuse_of_right_angled_triangle(side1, side2):
    return round((side1 ** 2 + side2 ** 2) ** 0.5, 2)

print hypotenuse_of_right_angled_triangle(3, 4)

