#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   pickle模块.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/13 11:36   luk      1.0         None
'''

# import lib

import pickle

def func():
    print("from func")

pickle.dump(func, open("pickle.txt", "wb"))
load = pickle.load(open("pickle.txt", "rb"))
print(load)
load()
