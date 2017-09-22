"""
39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""

amt = 10000
interest = 3.5
years = 7

# 如果利息按年结算, 本金会每年增加

for i in range(years):
    amt = amt * ( 1 + interest / 100.0)

print "%f" % amt


# 利息按七年结算

amt = 10000
interest = 3.5
years = 7

value = amt * ( 1 + interest / 100.0) ** years
print value