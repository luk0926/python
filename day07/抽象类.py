#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   抽象类.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/18 22:25   luk      1.0         None
'''

# import lib

import abc
class File(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def read(self):
        print("read")

class Text(File):
    def read(self):
        print("read")


t = Text()
t.read()
