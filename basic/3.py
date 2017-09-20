"""
3. Write a Python program to display the current date and time.
Sample Output : 
Current date and time : 
2014-07-05 14:34:14
"""

from datetime import datetime

now =  datetime.now()

print type(now)
print str(now)[:-7]
timeis = now.strftime("%Y-%m-%d %H:%M:%S") # string format by time
print timeis

print type(datetime.strptime(timeis, "%Y-%m-%d %H:%M:%S")) # string parse to time


