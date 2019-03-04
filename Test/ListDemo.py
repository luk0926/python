#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   ListDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/2 10:07   luk      1.0         None
'''

# import lib

a = ["a", "b", "c", "d"]
# print(a[0])
# print(len(a))
# print(a[1:2])
# a.append("e")
# print(a)
# for i in a:
#     print(i)

# 字典 dict
# v = {"name":"luk","age":18}
# print(v["name"])
# v["age"] = 20
# print(v)
# for i in v.keys():
#     print(i)
# for i in v.values():
#     print(i)
# for i,j in v.items():
#     print(i,j)

lst = [
    {"name":"aaa","pwd":"123","itimes":"1"},
    {"name":"bbb","pwd":"123","itimes":"1"},
    {"name":"ccc","pwd":"123","itimes":"1"}
]

name = input("请输入用户名：")
pwd = input("请输入密码：")
for i in lst:
    if name==i["name"] and pwd==i["pwd"]:
        print("登陆成功")
        break