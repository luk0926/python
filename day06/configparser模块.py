#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   configparser模块.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/13 21:20   luk      1.0         None
'''

# import lib

import configparser

config = configparser.ConfigParser()
config.read("prop.ini")

print(config.sections())
print(config.options("section1"))
print(config.items("section1"))
print(config.get("section1", "k1"))
config.remove_section("section1")
print(config.sections())