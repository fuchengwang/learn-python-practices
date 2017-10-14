"""
97. Write a Python program to list the special variables used within the language.
"""


print(set(globals().keys()) | set(__builtins__.__dict__.keys()))
