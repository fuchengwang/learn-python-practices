# _*_ coding:utf-8 _*_

"""
58. Write a python program to sum of the first n positive integers.
"""


def top_pos_number_sum(nums, n):
    count = 0
    result = 0

    for i in range(len(nums)):
        if count == n:
            break

        if nums[i] > 0:
            result += nums[i]
            count += 1

    return result

print top_pos_number_sum([1, -1, 2, -3], 0)
print top_pos_number_sum([1, -1, 2, -3], 1)
print top_pos_number_sum([1, -1, 2, -3], 2)
print top_pos_number_sum([1, -1, 2, -3], 3)
print top_pos_number_sum([1, 1], 2)



