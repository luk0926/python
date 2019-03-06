#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   FileDemo2.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/6 21:54   luk      1.0         None
'''

# import lib

# 拷贝图片
with open("图片.jpg","rb") as read_f,open("图片2.jpg","wb") as write_f:
    data = read_f.read()
    write_f.write(data)
print("拷贝成功")
