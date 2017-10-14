# _*_ coding: utf-8 _*_
"""
定义函数countchar()按字母表顺序统计字符串中所有出现的字母的个数（允许输入大写字符，并且计数时不区分大小写）。形如：
"""

def countchar1(str):
    table = dict(zip('abcdefghijklmnopqrstuvwxyz',[0]*26))

    for s in str.lower():
        if table.get(s) is not None:
            table[s] += 1
    return list(table.values())
        

# def countchar(str):
#     from collections import Counter
#     import string
#     c = Counter(str.lower())
#     table = dict(zip(string.ascii_lowercase, [0]*26))
#     return [c[k] for k in table]

def countchar(str):
    lst = [0] * 26

    for c in str.lower():
        if  97 <= ord(c) <= 122:
            lst[ord(c) - 97] += 1
    
    return lst

    

if __name__ == "__main__":
    import string
    print(type(countchar(string.printable)))
    print(type(countchar1(string.printable)))
    # while True:
    #     str = input()
    #     if countchar(str) != countchar1(str):
    #         print(countchar(str))
    #         print(countchar1(str))
    #     else:
    #         print('OK')
