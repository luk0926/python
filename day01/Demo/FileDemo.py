#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   FileDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/2 10:38   luk      1.0         None
'''

# import lib

f1 = open("db", "r")
data = f1.read()
# print(data)
split = data.split("\n")
user_info = []
for i in split:
    i_split = i.split("|")
    value = {
        "name":i_split[0],
        "pwd":i_split[1],
        "times":i_split[2]
    }
    user_info.append(value)
user_info[1]["times"] = 3
# print(user_info)

s = ""
for i in user_info:
    s += i["name"] + "|" + i["pwd"] + "|" + str(i["times"]) + "\n"

f2 = open("db2", "w")
f2.write(s)
f2.close()

