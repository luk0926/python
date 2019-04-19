#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   继承2.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/17 23:34   luk      1.0         None
'''

# import lib

class People:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def talk(self):
        print("%s talk" %self.name)


class Date:
    def __init__(self, year, month, day):
        self.year=year
        self.month=month
        self.day=day
    def birth(self):
        print("%s-%s-%s" %(self.year, self.month, self.day))

class Teacher(People):
    def __init__(self, name, age, sex, year, month, day):
        People.__init__(self, name, age)
        self.sex=sex
        self.year=year
        self.month=month
        self.day=day
        self.date = Date(self.year, self.month, self.day)


t = Teacher("luk", 18, "male", 1994, 3, 9)
print(t.name, t.age, t.sex, t.year, t.month, t.day)
t.date.birth()
t.talk()
