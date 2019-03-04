#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   FormatDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/3 14:12   luk      1.0         None
'''

# import lib
# 字符串的格式化 format
str1 = "姓名：{0}，年龄：{1}，性别：{2}"
str2 = str1.format("卢凯", 18, "男")
print(str1)
print(str2)

# 方式2
str3 = "姓名：{name},年龄：{age},性别：{gender}"
str4 = str3.format(name="卢凯", age=18, gender="男")
print(str3)
print(str4)

# format_map
str5 = "姓名：{name}，年龄：{age},性别：{gender}"
str6 = str5.format_map({"name":"卢凯","age":"18","gender":"男"})
print(str5)
print(str6)

str
