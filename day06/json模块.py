#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   json模块.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/13 10:33   luk      1.0         None
'''

# import lib

import json

# lst = "[null,true,false,1]"
# j1 = json.loads(lst)
# print(j1)
# res = json.dumps(lst)
# print(res)

# with open("json1.txt","w") as f:
#     res = json.dumps(lst)
#     f.write(res)

# with open("json1.txt", "r") as f:
#     read = f.read()
#     loads = json.loads(read)
#     print(loads)

dic = {"a":1, "b":2, "c":3}

json.dump(dic, open("json1.txt", "w"))
res = json.load(open("json1.txt", "r"))
print(res, type(res))
