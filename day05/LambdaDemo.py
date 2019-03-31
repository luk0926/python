#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   LambdaDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/28 21:21   luk      1.0         None
'''

# import lib

dic = {
    "d" : 100,
    "b" : 200,
    "c" : 300,
    "a" : 400
}

# res = zip(dic.values(), dic.keys())
# lst = list(res)

# print(max(dic, key=lambda k:dic[k]))
# print(min(dic, key = lambda k:dic[k]))
# print(sorted(dic, key=lambda k:dic[k],reverse=True))


# map函数的使用
# lst = ["a", "b", "c"]
# res = map(lambda x: x + "_sb", lst)
# print(list(res))

# from functools import reduce
# reduce函数的使用
# lst=[1, 2 , 3]
# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x+y,l,10))

# filter的用法
lst = ["a_sb", "b_sb","c_sb"]

res = filter(lambda x: x.endswith("sb"), lst)
print(list(res))


map()