#!/user/bin/python
# -*- conding:utf-8 -*-
'''
@File    :   Test3.py    
@Contact :   18514815382@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/2 11:50   luk      1.0         None
'''

# import lib

dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"]
    },
    "安徽": {
        "合肥": ["肥东", "肥西"],
        "亳州": ["蒙城", "涡阳"]
    }
}
for v in dic.keys():
    province = input("请输入省份：")
    for v1 in dic[province].keys():
        city = input("请输入市：")
        print(dic[province][city])
        break
    break
