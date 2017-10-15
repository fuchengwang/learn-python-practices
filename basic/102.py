"""
102. Write a Python program to get system command output.
"""
import os
import subprocess


def print_system_cmd_output(cmd):
    print(os.system(cmd))


def print_system_cmd_output_2(cmd):
    # universal_newlines参数若为True, 返回一个文本字符串. 默认返回的是二进制字符串
    print(subprocess.check_output(cmd, shell=True, universal_newlines=True))


print_system_cmd_output('ls -l')
print_system_cmd_output_2('cat ./mooc/monisen.py')
