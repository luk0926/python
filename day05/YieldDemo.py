#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   YieldDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/26 21:17   luk      1.0         None
'''

# import lib

def auth(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        next(res)
        return res
    return wrapper

@auth
def eater(name):
    print("%s is ready to eat" %name)
    food_list = []
    while True:
        food = yield food_list
        food_list.append(food)
        print("%s is ready to eat %s" %(name, food))


g = eater("luk")
print(g.send("脚指头1"))
print(g.send("脚指头2"))


