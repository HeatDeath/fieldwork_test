# -*- coding:utf-8 -*-
import sys


def hello_world():
    # print('hello_world!')
    print(sys._getframe().f_code.co_name)

if __name__ == '__main__':
    hello_world()