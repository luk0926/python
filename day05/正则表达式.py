#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   正则表达式.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/3 23:33   luk      1.0         None
'''

# import lib

import re

#  \w 匹配字母、数字、下划线 \W非字母数字下划线
# print(re.findall(r"a\wb", "a*b,a_b"))

# \d 匹配任意数字 \D 匹配任意非数字
print(re.findall(r"a\db", "a_ba2b"))

# . 匹配任意字符
print(re.findall(r"a.b", "aaba_b"))

# [] 匹配一组字符  [^..] 匹配不在[]中的字符，取反
print(re.findall(r"a[123]b", "a1ba2ba12b"))

# *：匹配0个或多个   +：匹配1个或多个    ？：匹配0个或1个
print(re.findall(r"a[0-9a-zA-Z]*b", "ab a0gHb a1b"))

# {n} :精确到n个   {n,m}:n到m个  {n,}至少n个
print(re.findall(r"a{1,3}b", "aab ab aaaab  a1b"))
print(re.findall(r"a{1,}b", "aab ab aaaab  a1b"))
print(re.findall(r"a{1}b", "aab ab aaaab  a1b"))

# a|b 匹配a或者b
print(re.findall(r"a|b", "abcab"))
print(re.findall("ab[123]+", "ab12"))

#  .*:贪婪匹配   .*？：非贪婪匹配
print(re.findall("a.*b",  "a  d  455b  sfas  b"))
print(re.findall("a.*?b",  "a  d  455b  sfas  b"))

# （）:匹配一个表达式
print(re.findall(r"(?:ab)+c", "ababc  ab"))