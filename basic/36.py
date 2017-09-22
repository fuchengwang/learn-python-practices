"""
36. Write a Python program to add two objects if both objects are an integer type. 
"""

def obj_add(a, b):
    if not type(a) == type(b) == int:
        raise TypeError('expected ints')
    return a+b


print obj_add(1, 2)
# print obj_add('as', 'a')


print type(1) == int
print type(1) is int
print isinstance(1, int)
print ''
print isinstance((2, 3), (str, tuple, list)) # str or tuple or list ?
print isinstance('hello' , (str, tuple, list))
