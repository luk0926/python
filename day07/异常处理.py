#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   异常处理.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/21 11:21   luk      1.0         None
'''

# import lib

try:
    mes = input(">>>")
    m = int(mes)

except ValueError as e:
    print(e)
finally:
    try:
        i = 1 + m
        print(i)
    except NameError as e:
        print(e)
