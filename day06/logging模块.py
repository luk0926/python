#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   logging模块.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/13 20:48   luk      1.0         None
'''

# import lib

import logging

logging.basicConfig(filename="access.log",
                    format="%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=10)
logging.info("info".encode("utf-8"))
logging.warning("warning".encode("utf-8"))
logging.error("error".encode("utf-8"))
