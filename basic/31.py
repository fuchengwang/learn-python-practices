# _*_ coding: utf-8 _*_
"""
31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

8 10  -> 8= (2*2)*2 , 20=(2*2)*5  => 最大公约数是4
15 25 -> 5

"""

def is_even(num):
    return num % 2 == 0

'逐一尝试法'
def gcd1(a, b):
    for i in range(min(a, b) // 2, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1


'分解因式法'

'辗转相除法'
def gcd2(a, b):

    if a % b == 0:
        return b
    
    return gcd2(b, a % b)
    

'更相减损法, 因为是减法, 所以递归的次数会比辗转相除法多'
def gcd3(a, b):
    print a, b
    
    if a <= 1 or b <=1:
        return 1

    if a == b:
        return a
    
    if a < b:
        a, b = b, a

    return gcd3(b, a-b)

# print gcd2(319 , 377)

print gcd1(319, 377)


