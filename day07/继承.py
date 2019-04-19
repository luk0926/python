#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   继承.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/17 23:12   luk      1.0         None
'''

# import lib

class Animal:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def talk(self):
        print("%s can talk" %self.name)

class People(Animal):
    def __init__(self, name, age, sex):
        Animal.__init__(self, name, age)
        self.sex=sex
    def talk(self):
        Animal.talk(self)
        print("%s say hello" %self.name)

class Dog(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
    def talk(self):
        Animal.talk(self)
        print("%s 哼哼" %self.name)


p = People("Alex", 18, "male")
d = Dog("佩奇", 8)
print(p.name, p.age, p.sex)
p.talk()
print(d.name, d.age)
d.talk()
