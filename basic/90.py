"""
90. Write a Python program to create a copy of its own source code.

Quine 是一个输出源码本身, 很多语言都可以实现, 虽然并没什么卵用..
"""


print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))())
