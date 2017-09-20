# _*_ coding: utf-8 _*_
"""
4. Write a Python program which accepts the radius of a circle from the user and compute the area. 
Sample Output : 
r = 1.1
Area = 3.8013271108436504
"""

import math


r = float(raw_input('input the radius:'))
print 'The area of the circle with radius', r, 'is:', math.pi * r ** 2 # **优先级大于*的优先级