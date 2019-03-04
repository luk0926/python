#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   IntputAndGetpass.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/25 22:26   luk      1.0         None
'''

# import lib

# 单行注释
"""
多行注释
"""

# 输入输出
user = input("请输入用户名：")
print(user)

import getpass
pwd = getpass.getpass("请输入密码：")
print(pwd)