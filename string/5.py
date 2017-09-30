'''
5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
'''

def swap(str1, str2):
    str1, str2 = (str2[:2] + str1[2:]), (str1[:2] + str2[2:])
    print(str1, str2)


swap('hello', 'world')