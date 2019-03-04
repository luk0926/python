#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   IfDemo2.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/25 22:54   luk      1.0         None
'''

# import lib

user_type = input("》》》")
if user_type == "root" :
    user = input("请输入管理员姓名：")
    if user == "luk" :
        print("欢迎：luk")
    else :
        print("管理员姓名输入有误！")
else :
    print("请重新输入！")