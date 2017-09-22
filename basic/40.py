"""
40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
"""

import math

def distance(point1, point2):
    x = abs(point1[0] - point2[0])
    y = abs(point1[1] - point2[1])

    return round(math.sqrt(x * x + y * y), 2)

p1 = (4, 0)
p2 = (6, 6)

print distance(p1, p2)