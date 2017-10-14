"""
83. Write a Python program to test if a certain number is greater than all numbers of a list.
"""


def is_bigger_than_list(n, lst):
    print(n > max(lst))


is_bigger_than_list(1, [1, 2, 3])
is_bigger_than_list(5, [1, 2, 3])
