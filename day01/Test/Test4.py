#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   Test4.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/2 15:16   luk      1.0         None
'''

# import lib

f1 = open("db", "r")
data = f1.read()
lst = data.split("\n")
new_lst = []
for i in lst:
    lst2 = i.split("|")
    dict = {
        "name":lst2[0],
        "pwd":lst2[1],
        "itimes":lst2[2]
    }
    new_lst.append(dict)

while True:
    name = input("请输入用户名：")
    pwd = input("请输入密码：")
    for dict2 in new_lst:
        if int(dict2["itimes"]) < 3:
            if dict2["name"] == name and dict2["pwd"] == pwd:
                print("登陆成功")
                break
            else:
                print("用户名或密码错误，请重试")
                dict2["itimes"] = str(int(dict2["itimes"])+1)
        else:
            print("登陆失败")
            break
