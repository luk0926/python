#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   装饰器Test.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/17 10:20   luk      1.0         None
'''

# import lib

# 执行主页登陆验证
import time

info = {"name":None, "status":False}

# 定义装饰器
def auth(func):
    def wrapper(*args, **kwargs):
        if info["name"] and info["status"]:
            func(*args, **kwargs)
            print("success")
        else:
            name = input("请输入用户名：")
            password = input("请输入密码：")
            if name=="luk" and password=="123":
                func(*args, **kwargs)
                print("success")
                info["name"]="luk"
                info["status"]=True
            else:
                print("err")
    return wrapper

@auth
def sign_in():
    time.sleep(0.5)
    print("welcome to home page")

@auth
def home_page(name):
    time.sleep(0.5)
    print("%s, welcome to homne page" %name)

sign_in()
home_page("luk")