#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   时间模块.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/10 22:37   luk      1.0         None
'''

# import lib

import time

# 时间戳
print(time.time())

# 结构化的时间
print(time.localtime())
print(time.gmtime())

# 格式化的时间
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# 时间相互转换
print(time.localtime(time.time()))

print(time.strftime("%Y %m %d %H:%M:%S", time.localtime()))
print(time.strptime("2019 04 10 22:46:46", "%Y %m %d %H:%M:%S"))