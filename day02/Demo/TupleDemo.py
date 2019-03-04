#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   TupleDemo.py
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/3 22:07   luk      1.0         None
'''

# import lib

# 元组：不可变的列表 不可变类型
tup = ("aa","bb",["cc","dd"],"ee")
tup[2][1]="10"
print(tup)