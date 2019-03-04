#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   ListDemo.py
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/3 15:52   luk      1.0         None
'''

# import lib

# extend:扩展，添加一个列表
# a_lst = ["a", 0, "b", 0.5]
# b_lst = ["ccc", 10]
# a_lst.extend(b_lst)
# print(a_lst)
# print(type(a_lst))

# sort:排序
a = [5,2,2,10]
# a.sort()  # 正序
# print(a)
a.sort(reverse=True)    # 倒序
print(a)