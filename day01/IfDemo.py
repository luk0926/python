#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   IfDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/25 22:41   luk      1.0         None
'''

# import lib

# if 1==1:
#     print("true")
# else:
#     print("false")

name = input("请输入用户名：")
import getpass
pwd = getpass.getpass("请输入密码：")

if name=="luk" and pwd == "123456" :
    print("登陆成功")
else :
    print("登录失败")