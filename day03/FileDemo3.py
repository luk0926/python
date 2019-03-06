#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   FileDemo3.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/6 22:25   luk      1.0         None
'''

# import lib

# 实现tail -f的功能

import time
with open("access.log","r") as f:
    while True:
        line = f.readline()
        if line and line not in ("\n","\t"):
            print(">>>  ",line)
        time.sleep(0.5)