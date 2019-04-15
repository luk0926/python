#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   test.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/15 21:39   luk      1.0         None
'''

# import lib

import os,sys

dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirname)

from core import run

if __name__==  "__main__":
    run.fun()