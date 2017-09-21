# _*_ coding: utf-8 _*_

"""
26. Write a Python program to create a histogram from a given list of integers.

    █         
    █         
█   █         
█   █   █     
█   █   █   █ 
█ █ █   █   █ 
█ █ █ █ █   █ 
█ █ █ █ █   █ 
6 3 8 2 5 0 4 

"""



def print_histogram(data):
    top = max(data)

    while top > 0:
        for n in data:
            if n >= top:
                print '█',
            else:
                print ' ',
        print ''
        top -= 1

    for n in data:
        print n,


lst = [6, 3, 8, 2, 5, 0, 4]
print_histogram(lst)

