#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   继承3.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/18 23:03   luk      1.0         None
'''

# import lib

class People:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def speak(self):
        print("People speak")

class Teacher(People):
    def __init__(self, name, age):
        super(Teacher, self).__init__(name, age)
        
    def speak(self):
        super(Teacher, self).speak()
        print("Teacher speak")


t = Teacher("luk", 18)
print(t.name, t.age)
t.speak()
