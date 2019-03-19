#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   装饰器2.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/18 21:54   luk      1.0         None
'''

# import lib

# import time
#
# def timmer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print("run time is %s" %(end_time - start_time))
#     return wrapper
#
# info={"name":None, "status":False}
#
# def auth(driver="file"):
#     def auth(func):
#         def wrapper(*args, **kwargs):
#             if driver=="file":
#                 print(">>>file")
#                 if info["name"] and info["status"]:
#                     func(*args, **kwargs)
#                     print("success")
#                 else:
#                     name = input("请输入用户名：")
#                     pwd = input("请输入密码：")
#                     if name=="luk" and pwd=="123":
#                         func(*args, **kwargs)
#                         print("success")
#                         info["name"]="luk"
#                         info["status"]=True
#                     else:
#                         print("error")
#             elif driver=="mysql":
#                 print(">>>mysql")
#                 func(*args,**kwargs)
#             else:
#                 print(">>>其他")
#         return wrapper
#     return auth
#
# @timmer
# @auth("file")
# def sign_in():
#     time.sleep(1)
#     print("welcome to home page")
#
# @timmer
# @auth("file")
# def home_page(name):
#     time.sleep(1)
#     print("%s, welcome to home page" %name)
#
# sign_in()
# home_page("luk")

# 迭代器
dic = {"a": 1, "b": 2, "c": 3}

i = dic.__iter__()
while True:
    try:
        print(i.__next__())
    except StopIteration:
        break
