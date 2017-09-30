'''
2. Write a Python program to count the number of characters (character frequency) in a string.
'''
import collections


def count(string):
    d = {}
    for s in string:
        d[s] = d.get(s, 0) + 1
    return d


r = count('google.com')
print(r)
    