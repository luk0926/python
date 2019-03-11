#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   FunctionDemo2.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/11 21:37   luk      1.0         None
'''

# import lib

# 可变长参数
# def fun1(x, y, *args):
#     print(x)
#     print(y)
#     print(args)
#
# fun1(1, 2, 3, 4, 5)

# def fun2(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# res1 = fun2(1, 2, 3, 4)
# print(res1)
# res2 = fun2(1, 2, 3, 4, 5)
# print(res2)

# def fun3(x, y, **kwargs):
#     print(x, y)
#     print(kwargs)
#
# fun3(x=1, y=2, name="叶炳娣",sex="female",age=14)

# def fun4(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# fun4(1, 2, 3, a="alex", b=18)

def foo(x, y, z):
    print(x, y, z)

def fun(*args, **kwargs):
    print(args)
    print(kwargs)
    foo(*args, **kwargs)

fun(1, z=3, y=2)