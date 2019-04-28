#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   Insert.py
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/24 22:43   luk      1.0         None
'''

# import lib

from pymysql import *

try:
    conn = connect(host="localhost", user="root", passwd="1234", db="python3")
    cursor = conn.cursor()

    sql = "insert into students values ('7', 'e', 1, '2019-01-02')"
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()

except Exception as e:
    print(e.message)





