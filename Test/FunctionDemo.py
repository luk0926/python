#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   FunctionDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/10 15:50   luk      1.0         None
'''

# import lib

# 函数：有参函数、无参函数、空函数

# 无参函数
def fun1():
    print("hello world")

# 有参函数
def fun2(a, b):
    # 三元表达式
    max = a if a > b else b
    return max

# 空函数
def fun3():
    pass

fun1()

max = fun2(10, 20)
print(max)

fun3()
