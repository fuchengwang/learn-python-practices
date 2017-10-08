#_*_ coding:utf-8 _*_
"""
54. Write a Python program to get the current username
"""


# getpass模块用来 提示用户输入密码，而不回显
# password = getpass.getpass('请输入密码')
import getpass 

print(getpass.getuser())


import os
print(os.getenv('USERNAME') or os.getenv('USER') or os.getenv('LOGNAME'))