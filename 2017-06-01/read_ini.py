# -*- coding:utf-8 -*-
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('read_ini.ini')

section_list = config.sections()
print(section_list)

option_list = config.options('baseconf')
print(option_list)

item_list = config.items('baseconf')
print(item_list)

db_host = config.get('baseconf', 'host')
print(db_host)

db_post = config.getint('baseconf', 'port')
print(db_post)