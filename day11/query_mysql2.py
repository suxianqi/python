#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'tedu',
    charset = 'utf8'
)
cursor = conn.cursor()

query1 = 'select * FROM departments'
cursor.execute(query1)
# cursor.scroll(2, mode='absolute') #从开头起始点移动游标
# r1 = cursor.fetchall() #取一行
# print(r1)0-
cursor.scroll(1,mode='absolute')  #从开头起始点移动游标
cursor.fetchone()                #取一行
cursor.scroll(1,mode='relative') #以当前位置位参考点移动游标
r2 = cursor.fetchall()  #取出后续所有内容
print(r2)

cursor.close()
conn.close()






