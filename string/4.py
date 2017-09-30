#_*_ coding: utf-8 _*_

'''
4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

把字符串与第一个字母相同的字符转换成$, 但是第一个不转换
'''

def change_char(string):
    return  string[0] + string[1:].replace(string[0], '$')
    

print(change_char('google'))

