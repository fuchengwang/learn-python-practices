"""
2. Write a Python program that matches a string that has an a followed by zero or more b's
"""

import re

re.search(r'ab*', 'oooa')
re.search(r'ab*', 'oooab')
re.search(r'ab*', 'oooabbbccc')


# an a followed one or more b's

re.search(r'ab+', 'oooaooo')
re.search(r'ab+', 'oooabooo')
