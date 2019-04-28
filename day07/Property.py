#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   Property.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/20 11:33   luk      1.0         None
'''

# import lib

class People:
    def __init__(self, height, weight):
        self.height=height
        self.weight=weight
    @property
    def bmi(self):
        return self.weight/self.height**2


p = People(1.75, 70)
print(p.bmi)

class Cir:
    def __init__(self, len, wid):
        self.len=len
        self.wid=wid
    @property
    def getZ(self):
        return (self.len + self.wid)*2
    @property
    def getM(self):
        return self.len*self.wid


c = Cir(10, 5)
print(c.getM)
print(c.getZ)