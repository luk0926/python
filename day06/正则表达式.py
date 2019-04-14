#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   正则表达式.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/10 21:33   luk      1.0         None
'''

# import lib

# 正则表达式
import re
print(re.split("ab", "abcab"))

print(re.sub("^a", "A", "alex make love"))