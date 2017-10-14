"""
94. Write a Python program to convert a byte string to a list of integers.
"""

bytes = b'hello world'

binary = bin(int(bytes.hex(), 16))
print(list(binary))


# ascii list
print(list(bytes))
