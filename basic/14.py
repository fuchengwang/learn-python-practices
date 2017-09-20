"""
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

from datetime import date

day1 = date(2014, 7, 2)
day2 = date(2014, 7, 11)

delta = day2 - day1
print delta.days