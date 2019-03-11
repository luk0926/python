#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   FunctionDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/7 23:31   luk      1.0         None
'''

# import lib

# 函数：有参函数、无参函数、空函数
def fun1():
    # 无参函数
    print("hello world")

def fun2(a, b):
    # 三元表达式
    # 传入参数：a、b，返回两者中最大值
    max = a if a > b else b
    return max

def fun3():
    # 空函数
    pass

fun1()
max = fun2(10, 20)
print(max)
fun3()