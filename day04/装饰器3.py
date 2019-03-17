#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   装饰器3.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/16 15:37   luk      1.0         None
'''

# import lib

# 装饰器
import time

# 定义装饰器timmer
def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("run time is %s" %(end_time - start_time))
        return res
    return wrapper

@timmer
def index():
    time.sleep(1)
    print("hello index")
    return 1

@timmer # timmer(index)
def index2(name):
    time.sleep(1)
    print("my name is %s" %name)


res = index()
print(res)
index2("index")
