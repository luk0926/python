#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   EnumrateDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/3 20:50   luk      1.0         None
'''

# import lib

lst = ["aa","bb","cc"]
for i,ele in enumerate(lst,1):
    print(i,ele)

num = input("请输入序号：")
num = int(num)
print(lst[num-1])
