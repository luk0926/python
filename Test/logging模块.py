#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   logging模块.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/15 21:21   luk      1.0         None
'''

# import lib

import logging
# logging.basicConfig(filename="a.txt",
#                     format="%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(message)s",
#                     datefmt="%Y-%m-%d %H:%M:%S",
#                     level=10)
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")

logging.basicConfig(format="%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=10)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")