# _*_ coding: utf-8 _*_

"""
27. Write a Python program to concatenate all elements in a list into a string and return it.
"""

'加号拼接法: 每次拼接都要申请新的内存空间, 产生很多无用的中间结果, 效率低'
def concat_list(lst):
    s = ''
    for item in lst:
        s += str(item)
    return s


'join拼接法 : 一次性完成拼接,效率高'
def concat_list_by_join(lst):
    return ''.join([str(i) for i in lst])

print concat_list([1, 2, 3])
print concat_list_by_join([4, 5, 6])