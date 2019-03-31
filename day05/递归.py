#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   递归.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/28 22:19   luk      1.0         None
'''

# import lib
# def f1():
#     print("from f1")
#     def f2():
#         print("from f2")
#         f1()
#     f2()
# f1()

# def age(n):
#     if n==1:
#         return 18
#     return age(n-1)+2
#
# print(age(5))

# 二分查找
lst = [1, 3, 8, 15, 85, 102, 155]
def search(num, seq):
    if len(seq)==0:
        print("%s not exists" %num)
        return
    mid_len = len(seq) // 2
    print(seq, seq[mid_len])
    if num > seq[mid_len]:
        seq = seq[mid_len+1:]
        search(num, seq)
    elif num< seq[mid_len]:
        seq = seq[:mid_len-1]
        search(num, seq)
    else:
        print("find it")

search(9, lst)