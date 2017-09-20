# _*_ coding: utf-8 _*_

"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
"""

exam_st_date = (11, 12, 2014)

"转化成时间后输出格式化的时间字符串"
from datetime import datetime
d = datetime(exam_st_date[2], exam_st_date[1], exam_st_date[0])
print d.strftime("%d / %m / %Y")

"直接格式化输出"
print "The examination will start from : %d / %d / %d" % exam_st_date