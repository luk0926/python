#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   IfDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/26 20:55   luk      1.0         None
'''

# import lib

# 请输入用户名
# user = input("请输入用户名：")
#
# import getpass
#
# password = getpass.getpass("请输入密码：")
#
# if user=='luk' and password=='123':
#     print("登陆成功")
# else:
#     print("登陆失败")

type = input("》》》")
if type == 'root':
    name = input('请输入用户名：')
    if name=='luk':
        print('你真帅')
    elif name=='sb':
        print("滚蛋")
    else:
        print('请输入正确的用户名')
else:
    pass