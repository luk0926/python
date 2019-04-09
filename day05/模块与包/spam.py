#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   spam.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/31 10:15   luk      1.0         None
'''

# import lib

# __all__ = ["money"]
# print(" from spam")
# money = 1000
# def read1():
#     print("from spam -> read1 -> money %s" %money)
#
# def read2():
#     global money
#     money = 0
#
# print(__name__)

from aaa.bbb import pkg as a
print(a.money)