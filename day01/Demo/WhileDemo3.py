#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   WhileDemo3.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/26 22:36   luk      1.0         None
'''

# import lib

# 模拟用户登陆 最多3次
# i = 1
# while True:
#     name = input("请输入用户名：")
#     pwd = input("请输入密码：")
#     if name=='luk' and pwd=='123':
#         print("登陆成功")
#         break
#     else:
#         if i==3:
#             print("用户名或密码错误，登陆失败")
#             break
#         else:
#             print("用户名或密码错误，请重试")
#     i+=1

# 猜数字,三次机会
value = 7
i = 1
while i<=3:
    guess = input("请输入你要猜的数字：")
    if int(guess) == value:
        print("恭喜你，猜中了")
        break
    else:
        if i==3:
            print("你已经没有机会了")
        else:
            print("猜错了，请重试")
    i+=1