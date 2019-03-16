#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   Fun1.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/13 22:20   luk      1.0         None
'''

# import lib

# 函数的嵌套使用

# def fun1(a,b):
#     res = a if a > b else b
#     return res
#
# def fun2(a,b,c,d):
#     res = fun1(fun1(fun1(a, b), c), d)
#     print(res)
#
# fun2(1,2,3,4)
#

# 函数的嵌套
def fun1():
    def fun2():
        print("fun2")
        def fun3():
            print("fun3")
        fun3()
    fun2()
fun1()