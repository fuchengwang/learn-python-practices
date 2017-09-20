"""
12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. 
"""

import calendar

year = int(raw_input("the year: "))
month = int(raw_input("the month: "))

# txt_cal = calendar.TextCalendar()
# txt_cal.prmonth(year, month)

calendar.prmonth(year, month)