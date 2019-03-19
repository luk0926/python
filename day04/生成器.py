#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   生成器.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/19 21:20   luk      1.0         None
'''

# import lib

import time


def tail(file):
    with open(file, "r") as f:
        while True:
            line = f.readline().strip()
            if line:
                yield line
            else:
                time.sleep(0.5)


def grep(patten, line):
    for i in line:
        if patten in i:
            print(i)


grep("python", tail("a.txt"))
