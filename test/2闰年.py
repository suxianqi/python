#!/usr/bin/env python
# -*- coding: UTF-8 -*-


yeas = int(input("请输入查询的年份： "))
if yeas % 4 ==0 and yeas % 100 !=0:
    print('这个是闰年')
else:
    print('不是闰年')