#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   装饰器Test2.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/17 20:25   luk      1.0         None
'''

# import lib
# 有参装饰器

import time

info = {"name":None, "status":False}

# 定义一个有参装饰器
def auth(driver = "file"):
    def auth2(func):
        def wrapper(*args, **kwargs):
            if driver=="file":
                print("======file")
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
            elif driver=="mysql":
                print("=====mysql")
                func(*args, **kwargs)

        return wrapper
    return auth2

@auth(driver = "file")
def sign_in():
    time.sleep(1)
    print("welcome to home page")

@auth("mysql")
def home_page(name):
    time.sleep(1)
    print("%s, welcome to home page" %name)

sign_in()
home_page("luk")