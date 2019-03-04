#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   DictDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/1 21:59   luk      1.0         None
'''

# import lib

# 字典
v = {"name":"luk", "age":18}
# print(v)

# 获取值
# print(v["name"])
# 增加或修改
# v["age"] = 20
# print(v)
# 删除
# del v["name"]
# print(v)
# 循环
# for i in v.keys():
#     print(i)
# for i in v.values():
#     print(i)
# for i in v.items():
#     print(i)
for i,j in v.items():
    print(i, j)