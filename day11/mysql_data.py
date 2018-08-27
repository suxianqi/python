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
insert_dep1 = 'INSERT INTO departments VALUES(%s, %s)'
# cursor.execute(insert_dep1,('1', '人事部'))   #单条插入
insert_deps = [(2,'运维部'),(3,'开发部'),(4,'测试部')]
cursor.executemany(insert_dep1,insert_deps)   #多条语句插入  效率快
conn.commit()
cursor.close()
conn.close()
print('执行成功')

