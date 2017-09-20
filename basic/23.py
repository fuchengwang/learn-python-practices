"""
23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
"""

def cut_string(str, time):
   return str[:2] * time

print cut_string('hello', 2)
print cut_string('h', 3)