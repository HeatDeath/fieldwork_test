# -*- coding:utf-8 -*-
# 单纯的使用 logging 将 数据 写入 .log 文件
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    # w 为覆盖 ， a 为追加
                    filemode='w')
test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in xrange(5):
    logging.debug(test)