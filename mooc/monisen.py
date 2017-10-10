# _*_ coding:utf-8 _*_
"""
寻找第n个莫尼森数

如果两个素数P, M , 满足 M = 2 ** P -1, 则称M为莫尼森数
"""

def prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def monisen(n):
    counter = 0

    i = 2
    while True:
        if prime(i) and prime(2 ** i - 1):
            counter += 1
            if counter == n:
                break
        i += 1

    return 2 ** i - 1

print(monisen(4))
