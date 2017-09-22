"""
35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
"""

def number_test(a, b):
    return a == b or a + b == 5 or abs(a - b) == 5

print number_test(1, 1)
print number_test(6, 1)
print number_test(1, 6)
print number_test(2, 3)
print number_test(10, 18)


