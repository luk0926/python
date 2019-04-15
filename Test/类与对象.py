#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   类与对象.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/15 21:53   luk      1.0         None
'''

# import lib

class Chinese:
    country = "China"
    def __init__(self, name, age, sex):
        self.Name=name
        self.Age=age
        self.Sex=sex
    def talk(self):
        print("%s talk" %self.Name)


p1 = Chinese("luk", 18, "male")
print(p1.Name, p1.Age, p1.Sex, p1.country)
p1.talk()
