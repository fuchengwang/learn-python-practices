# _*_ coding: utf-8 _*_
"""
7. Write a Python program to accept a filename from the user and print the extension of that. 
"""

filename = raw_input("input file name: ")

'从右索引 然后 分片法'
index = filename.rfind('.') 
if index != -1:
    print filename[index+1:]

'split法'
print filename.rsplit('.', 1)[-1]  # 从右边开始分裂, 最大分裂次数为1次


    