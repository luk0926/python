#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   Test2.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/2 11:30   luk      1.0         None
'''

# import lib
v = 2000
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

while True:
    num = input("请输入商品序号：0：电脑，1：鼠标，2：游艇，3：美女，4：结束  >>>")
    num = int(num)
    if num in [0, 1, 2, 3]:
        v -= goods[num]["price"]
        if v > 0:
            print("您购买的商品为：" + str(goods[num]) + ",余额：" + str(v))
        else:
            print("余额不足！")
            break
    elif num == 4:
        print("购买结束，您的余额为：" + str(v))
        break
    else:
        print("请输入正确编号！")
