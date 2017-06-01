# -*- coding:utf-8 -*-
import os
import sys

# 当前文件在系统中的绝对路径
print(os.path.abspath(__file__))

# 上级目录
print(os.path.pardir)

# 当前文件及兄弟文件（夹）
print(os.path.join(os.path.dirname(__file__), os.path.pardir))

# 当前文件所在的目录
print(os.path.dirname(os.path.abspath(__file__)))

# 当前文件所在目录的上级目录
print(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))