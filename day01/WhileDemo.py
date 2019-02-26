#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   WhileDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/26 22:07   luk      1.0         None
'''

# import lib

# 打印1 2 3 4 5 6 8 9 10
i = 1
# while True:
#     if i==7:
#         pass
#     else:
#         print(i)
#     i += 1
#
#     if i==11:
#         break
# print('end')

while True:
    if i==7:
        i+=1
        continue
    print(i)
    i+=1
    if i==11:
        break
print("end")