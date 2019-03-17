#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   装饰器.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/17 9:33   luk      1.0         None
'''

# import lib

import time

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

@timmer
def index2(name):
    time.sleep(1)
    print("my name is %s" %name)


# res = timmer(index)()
# print(res)
# timmer(index2)("index2")

res = index()
print(res)
index2("index2")
