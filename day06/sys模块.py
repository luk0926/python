#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   sys模块.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/12 22:40   luk      1.0         None
'''

# import lib

import sys

print(sys.argv)

print(sys.path)

import shutil

shutil.copyfileobj(open("os模块.py","r"), open("copy.txt", "w"))
shutil.copyfile("copy.txt", "copy2.txt")
