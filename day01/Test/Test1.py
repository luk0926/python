#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   Test1.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/2 11:27   luk      1.0         None
'''

# import lib

v1 = [11,22,33,44,55,66,77,88,99,90]
v2 = []
v3 = []
for i in v1:
    if i>66:
        v2.append(i)
    else:
        v3.append(i)
v4 = {
    "k1":v2,
    "k2":v3
}
print(v4)