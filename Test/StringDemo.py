#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   StringDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/1 20:47   luk      1.0         None
'''

# import lib

# 查看数据类型
# a = "10"
# print(type(int(a)))

# python的占位符,%s,%d
# a = "姓名：%s,年龄：%d"
# b = a %("卢凯", 18)
# print(b)

a = input("》》》")
i = 0
j = len(a)
while i <j:
    print(a[i])
    i+=1