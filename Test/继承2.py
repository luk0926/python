#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   继承2.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/19 23:28   luk      1.0         None
'''

# import lib

class People:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def speak(self):
        print("people speak")

class Teacher(People):
    def __init__(self, name, age, sex):
        super(Teacher, self).__init__(name, age)
        self.sex=sex
    def speak(self):
        super(Teacher, self).speak()
        print("teacher speak")

class Student(People):
    def __init__(self, name, age):
        super(Student, self).__init__(name, age)
    def speak(self):
        print("student speak")

def fun(obj):
    obj.speak()


t = Teacher("luk", 8, "male")
s = Student("佩奇",85)
print(t.name, t.age, t.sex)
fun(s)
fun(t)
