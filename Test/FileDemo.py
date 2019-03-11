#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   FileDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/7 22:22   luk      1.0         None
'''

# import lib

# 拷贝一张图片
# with open("图片.jpg","rb") as read_f, open("图片2.jpg","wb") as write_f:
#     data = read_f.read()
#     write_f.write(data)
# print("拷贝成功")

# 实现tail -f的功能
# import time
# with open("a.txt","r") as read_f:
#     while True:
#         line = read_f.readline()
#         if line and line not in ("\t","\n","\r"):
#             print(">>>",line)
#         time.sleep(0.5)

f = open("a.txt", "r")
data = f.read()
print(data)
f.close()
