#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   hashlib模块.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/13 17:22   luk      1.0         None
'''

# import lib

import hashlib

# m = hashlib.md5()
# m.update("abc".encode("utf-8"))
# print(m)
# print(m.hexdigest())

# md5加盐
m = hashlib.md5("abcdefg".encode("utf-8"))
m.update("abc".encode("utf-8"))
print(m.hexdigest())
