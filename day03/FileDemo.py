#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   FileDemo.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/6 21:23   luk      1.0         None
'''

# import lib

with open("a.txt","r") as f_r, open("b.txt", "w") as f_w:
    for line in f_r:
        f_w.write(line)
    else:
        print("写入文件结束")