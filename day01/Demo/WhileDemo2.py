#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   WhileDemo2.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/26 22:22   luk      1.0         None
'''

# import lib

# 计算1-100之和
# sum = 0
# i = 1
# while i <=100:
#     sum += i
#     i += 1
# print(sum)

# 输出1-100以内所有奇数
# i = 1
# while i<=100:
#     if i%2==1:
#         print(i)
#     i += 1

# 求1-2+3-4+5...99之和
i = 1
sum = 0
while i<100:
    if i%2==0:
        sum = sum-i
    else:
        sum = sum + i
    i+=1
print(sum)