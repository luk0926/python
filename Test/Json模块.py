#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   Json模块.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/15 21:07   luk      1.0         None
'''

# import lib

import json
str = "[null,true,false,1]"
lst = json.loads(str)
# print(lst, type(lst))
dumps = json.dumps(lst)
# print(dumps, type(dumps))

lst = ["a", "b", "c"]
# json.dump(lst, open("a.txt", "w"))
# load = json.load(open("a.txt", "r"))
# print(load)

import pickle

def fun():
    print("from fun")

# pickle.dump(fun, open("a.txt", "wb"))
# load = pickle.load(open("a.txt", "rb"))
# load()
