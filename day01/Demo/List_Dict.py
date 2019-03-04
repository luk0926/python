#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   List_Dict.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/1 22:15   luk      1.0         None
'''

# import lib

# 列表和字典的嵌套
user_info = [
    {"name":"luk","pwd":"123123","times":1},
    {"name":"abc","pwd":"123123","times":1},
    {"name":"alex","pwd":"123123","times":1}
]

name = input("请输入用户名：")
pwd = input("请输入密码：")
for i in user_info:
    if name==i["name"] and pwd==i["pwd"]:
        print("登陆成功")
        break