#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   TypeDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/27 22:30   luk      1.0         None
'''

# import lib

# 数据类型
# type 查看数据类型
# a = 10
# print(type(a))
# print(type(str(a)))

# 整数 int
# a = "10"
# print(int(a))

# 布尔值 bool
# print(bool(0))
# print(bool(1))
# print(bool(-1))
# print(bool(""))
# print(bool("  "))

# 字符串 str
# a = 10
# print(str(a))
# 字符串的拼接
# a = "Alex "
# b = "sb"
# print(a + b)
# 格式化   %s/%d：占位符
# a = "我的名字叫：%s，我今年：%d岁"
# b = a %("luk", 19)
# print(b)
# 移除空白
# a = " alex "
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
# 分割
# a = "abc|123|???"
# print(a.split("|"))
# print(a.split("|", 1))
# print(a.rsplit("|", 1))
# 长度 len
# a = "卢凯sb"
# print(len(a))
# 索引
# a = "卢凯SB"
# print(a[0])

# a = input(">>>")
# i = 0
# l = len(a)
# while i<l:
#     print(a[i])
#     i+=1

# 切片
a = "我叫卢凯，我今年18岁"
print( a[2:6] )
print( a[2:8:2] ) # 指定步长为2
print( a[2:-2] )
print( a[2:] )
print( a[-2: ] )