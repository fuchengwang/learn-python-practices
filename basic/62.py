"""
62. Write a Python program to convert all units of time into seconds.
"""

from datetime import timedelta




delta = timedelta(days=3, hours=8)
print delta.total_seconds()
