#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   start.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/14 10:51   luk      1.0         None
'''

# import lib

import os,sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from core.run import fun
if __name__=="__main__":
    fun()
