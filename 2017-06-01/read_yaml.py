# -*- coding:utf-8 -*-
import os
import yaml


current_path = os.path.abspath(os.path.dirname(__file__))
print(current_path)
print(current_path + '/../test_dir')

with open(current_path + '/test_dir/' + 'read_yaml.yaml', 'r') as f:
    temp = yaml.load(f.read())
    print(temp)
    print(temp['basic_name'])
    print(temp['basic_name']['test_name'])
    print(temp['basic_name']['selected_name'][0])