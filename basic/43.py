# _*_ coding: utf-8 _*_

"""
 Write a Python program to get OS name, platform and release information.

 操作系统内部信息的库是 platform
 操作系统接口库 os
"""

import platform
import os



print os.name
print os.uname()

print '\n'

print platform.platform() # 汇总
print platform.uname()
print platform.system()  # os name
print platform.release() # os release info
print platform.machine() # 架构

print platform.node() # 网络名称
