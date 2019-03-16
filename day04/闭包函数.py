#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   闭包函数.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/14 22:28   luk      1.0         None
'''

# import lib

# 闭包函数：内部函数对外部空间但不包括全局作用域的引用，这个函数就是闭包函数
def foo(x):
    def fun():
        print(x)
    return fun


f = foo(1)
f()
