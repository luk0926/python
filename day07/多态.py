#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   多态.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/18 23:34   luk      1.0         None
'''

# import lib

class Animal:
    def talk(self):
        print("animal talk")

class People(Animal):
    def talk(self):
        print("people talk")

class Pig(Animal):
    def talk(self):
        print("pig talk")


p1 = People()
p2 = Pig()
# p1.talk()
# p2.talk()
def fun(obj):
    obj.talk()

fun(p1)
fun(p2)
