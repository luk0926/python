#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   run.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/14 10:51   luk      1.0         None
'''

# import lib

import hashlib

def fun():
     m = hashlib.md5("abc".encode("utf-8"))
     m.update("adghda".encode("utf-8"))
     print(m.hexdigest())
