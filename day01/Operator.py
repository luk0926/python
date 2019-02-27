#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   Operator.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/27 21:46   luk      1.0         None
'''

# import lib

# 运算符
# %：取模
# **：幂
# in
# not in

a = 10
b = 3
print(a % b) # 1
print(a ** b) # 1000

str = "Alex 前几天去泰国游玩"
c = "泰国"
if c in str:
    print("包含敏感词汇")
else:
    print(str)