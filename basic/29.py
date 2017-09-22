# _*_ coding: utf-8 _*_
"""
29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

Test Data : 
    color_list_1 = set(["White", "Black", "Red"]) 
    color_list_2 = set(["Red", "Green"])
Expected Output : 
    {'Black', 'White'}
"""



color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

# 两个集合相同或不同的元素集合 O(n^2)
print [c for c in color_list_1 if c not in color_list_2]

# set的一个方法 difference()
print color_list_1.difference(color_list_2)

# set1 - set2 
print color_list_1 - color_list_2

