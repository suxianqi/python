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

# delele = 'DELETE FROM departments WHERE dep_name = %s'
# cursor.execute(delele,('测试部',))
# update_dep ='update departments set dep_name=%s WHERE dep_name=%s'
# cursor.execute(update_dep,('人力资源部','人事部'))
add_sql = 'insert into departments VALUES (%s,%s)'
cursor.execute(add_sql,('4','测试部'))


conn.commit()



cursor.close()
conn.close()






