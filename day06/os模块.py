#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   os模块.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/12 22:36   luk      1.0         None
'''

# import lib

import os

path = os.path.abspath("os模块.py")
print(path)

print(os.path.exists("os模块.py"))
print(os.path.getsize("os模块.py"))