#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   ClassTest.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/17 21:37   luk      1.0         None
'''

# import lib


class Foo:
    count = 0
    def __init__(self):
        Foo.count += 1


f1 = Foo()
f2 = Foo()

print(Foo.count)
print(f1.count)
