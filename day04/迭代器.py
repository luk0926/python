#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   迭代器.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/17 22:29   luk      1.0         None
'''

# import lib

# 迭代器
# dic = {"a":1, "b":2, "c":3}
# i = dic.__iter__()
# while True:
#     try:
#         print(dic[i.__next__()])
#     except StopIteration:
#         break

# from collections import Iterable, Iterator
#
# lst = ["a", "b", 1, 2]
# i = lst.__iter__()
# print(isinstance(lst, Iterable))
# print(isinstance(i, Iterator))

dic = {"a":1, "b":2}
i = dic.__iter__()
while True:
    try:
        key = i.__next__()
        print(dic[key])
    except StopIteration:
        break
