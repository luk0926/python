#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   封装.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/20 11:05   luk      1.0         None
'''

# import lib

class People:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print("姓名：%s, 年龄：%s"%(self.name, self.age))

class Teacher(People):
    def __init__(self, name, age):
        super(Teacher, self).__init__(name, age)
    def info(self):
        super(Teacher, self).info()
    def set_info(self, set_name, set_age):
        if not isinstance(set_name, str):
            raise TypeError("set_name为str类型")
        if not isinstance(set_age, int):
            raise TypeError("set_age为int；类型4")
        self.name=set_name
        self.age=set_age


t = Teacher("luk", 12)
t.info()

t.set_info("alex", 18)
t.info()
