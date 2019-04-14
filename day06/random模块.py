#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   random模块.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/11 22:52   luk      1.0         None
'''

# import lib

import random

print(random.random())
print(random.randint(2,3))

lst = ["a", "b", "c"]
print(random.choice(lst))
print(random.choices(lst))

# 模拟验证码
def getCode(n):
    code = ""
    for i in range(n):
        num = random.randint(0, 9)
        s = chr(random.randint(65,90))
        add = str(random.choice([num, s]))
        code+=add
    return code


code = getCode(6)
print(code)

