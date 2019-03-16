#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   装饰器.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/16 10:46   luk      1.0         None
'''

# import lib

# 装饰器其实就是函数
# 装饰器的作用是在不更改源代码的情况下为添加新功能

# 给index函数添加运行时间功能

# demo1
# import time
# def index():
#     start_time = time.time()
#     time.sleep(3)
#     print("hello index")
#     end_time = time.time()
#     print("run time is %s" %(end_time - start_time))
#
# index()

# demo2
# import time
# def timmer():
#     start_time = time.time()
#     index()
#     end_time = time.time()
#     print("run time is %s" %(end_time-start_time))
#
# def index():
#     time.sleep(3)
#     print("hello index")
#
# timmer()

# demo3
# import time
#
# def timmer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         end_time = time.time()
#         print("run time is %s" %(end_time - start_time))
#     return wrapper
#
# @timmer
# def index():
#     time.sleep(3)
#     print("hello index")
#
# index()

# demo4
import time


def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("run time is %s" % (end_time - start_time))

    return wrapper


@timmer
def index():
    time.sleep(3)
    print("hello index")


index
