# -*- coding:utf-8 -*-
import sys


class testsqawd(object):
    def hello(self):
        print('the name of method is ## {} ##'.format(sys._getframe().f_code.co_name))
        print('the name of class is ## {} ##'.format(self.__class__.__name__))


if __name__ == '__main__':
    ttt = testsqawd()
    ttt.hello()

