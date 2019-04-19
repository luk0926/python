#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   继承.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/18 21:29   luk      1.0         None
'''

# import lib

class People:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def speak(self):
        print("%s can speak"  %self.name)

class Date:
    def __init__(self, year, month, day):
        self.year=year
        self.month=month
        self.day=day
    def birth(self):
        print("%s-%s-%s" %(self.year, self.month, self.day))

class Teacher(People):
    def __init__(self, name, age, year, month, day):
        People.__init__(self, name, age)
        self.year=year
        self.month=month
        self.day=day
        self.date=Date(self.year, self.month, self.day)

t = Teacher("alex", 18, 2019, 5, 20)
t.date.birth()
