#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   WhileDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/27 21:15   luk      1.0         None
'''

# import lib

#  模拟登陆 三次机会
i = 1
while True:
    name = input("请输入用户名：")
    pwd = input("请输入密码：")

    if i<3:
        if name == "luk" and pwd == "123":
            print("登陆成功！")
            break
        else:
            print("用户名或密码错误，请重试")
            i+=1
    else:
        print("用户名或密码错误，登陆失败")
        break