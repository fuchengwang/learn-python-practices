# _*_ coding: utf-8 _*_

"""
33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

多个数 要比较 两两相等, 可以用set
"""

def my_sum(a, b, c):
    if len(set([a, b, c])) < 3:
        return 0
    else:
        return a+b+c

print my_sum(1, 2, 3)
print my_sum(1, 1, 2)
print my_sum(1, 1, 1)


# 改进为兼容多个数

def my_sum2(lst):
    if len(set(lst)) < len(lst):
        return 0
    else:
        return sum(lst)

print my_sum2([1, 2, 3, 4, 5])
print my_sum2([1, 1, 2])
print my_sum2([1, 1, 1])

# 简写
def my_sum3(lst):
    return (lambda l: 0 if len(set(l)) < len(l) else sum(l))(lst)

print my_sum3([1, 2, 3, 4, 5])
print my_sum3([1, 1, 2])
print my_sum3([1, 1, 1])