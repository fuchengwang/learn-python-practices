"""
11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
Sample function : abs()
Expected Result : 
abs(number) -> number
Return the absolute value of the argument.
"""
import pydoc

print 30 * '='
help(abs)

print 30 * '='
pydoc.doc(abs)

print 30 * '='
print pydoc.getdoc(abs)

print 30 * '='
print abs.__doc__