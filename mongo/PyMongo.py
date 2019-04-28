#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   PyMongo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/28 22:05   luk      1.0         None
'''

# import lib

from pymongo import *

client = MongoClient("localhost", 27017)
db = client.tmp
collection = db.stu2

# 插入数据
# collection.insert({"name":"f", "gender":"f", "age":25})

# 修改操作
# collection.update({"name":"f"}, {"$set":{"name":"g"}})

# 删除数据
# collection.delete_one({"name":"g"})

# 查询数据
# cursor = collection.find()
# for s in cursor:
#     print(s["name"])

cursor = collection.find({"age": {"$gt": 15}}).sort("age", -1).skip(1).limit(2)
for s in cursor:
    print(s["name"], s["age"])