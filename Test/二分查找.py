#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   二分查找.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/31 9:25   luk      1.0         None
'''


# import lib

def search(num, seq):
    mid_len = len(seq) // 2
    print(seq, seq[mid_len])
    if mid_len == 0:
        print("%s not exists" % num)
        return
    if num > seq[mid_len]:
        seq = seq[mid_len:]
        search(num, seq)
    elif num < seq[mid_len]:
        seq = seq[:mid_len]
        search(num, seq)
    else:
        print("%s  exists" % num)

lst = [1,3,5,7,9]
search(10, lst)