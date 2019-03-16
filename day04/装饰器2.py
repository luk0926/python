#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   装饰器2.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/16 13:17   luk      1.0         None
'''

# import lib

import time
def fun(index):
    def wrapper():
        start_time = time.time()
        index()
        end_time = time.time()
        print("run time is %s" %(end_time - start_time))
    return wrapper

@fun
def  index():
    time.sleep(3)
    print("hello index")

index()