# _*_ coding: utf-8 _*_

"""
32. Write a Python program to get the least common multiple (LCM) of two positive integers. 


两个或多个整数公有的倍数叫做它们的公倍数，其中除0以外最小的一个公倍数就叫做这几个整数的最小公倍数

最小公倍数=两数的乘积/最大公约（因）数, 
"""

def lcm(a, b):
    i = max(a, b)

    while True:
        if i % a == 0 and i % b == 0:
            return i
        i += 1
    
print lcm(12, 17)
print lcm(4, 6)


def lcm2(a, b):
    import fractions
    return a * b / fractions.gcd(a, b)

print lcm2(12, 17)
print lcm2(4, 6)



