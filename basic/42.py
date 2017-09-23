# _*_ coding: utf-8 _*_
"""
42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

测试机器是64位还是32位
"""

import sys
import platform
import struct

is_64bits = sys.maxsize > 2**32

print is_64bits  # 如果是64位  sys.maxsize 要大于 2**32

print struct.calcsize('P') * 8  # 32位输出32, 64位输出64

platform.architecture()[0] # 获取操作系统可执行程序的结构, 如('32bit', 'ELF')