#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from  db_conn_sqlalchemy import Session,Departments,Employees,Salary

# hr = Departments(dep_name='hr')
# print(hr.dep_id)   #此是还没有在数据库中创建记录,所以是None

# op = Departments(dep_id=2,dep_name='运维部')
# print(op.dep_name)

# print(op)
# dev =Departments(dep_id=3,dep_name='开发部')
# qa = Departments(dep_id=4,dep_name='测试部')
# ha = Departments(dep_name='asd部')


# bob = Employees(emp_id=1, emp_name='BOb',gender='male',birth_date='2000-01-1',email='bob@qq.com',dep_id='4')
# jack = Employees(emp_id=2, emp_name='Jack',gender='male',birth_date='1995-07-31',email='jack@qq.com',dep_id='2')
# tom = Employees(emp_id=3, emp_name='Tom',gender='female',birth_date='1990-01-1',email='tom@163.com',dep_id='3')
# jane = Employees(emp_id=4, emp_name='Jane',gender='female',birth_date='1988-01-1',email='bob@qq.com',dep_id='1')
sal1 = Salary( auto_id='1', date ='2018-08-27',emp_id ='2',basic ='10000', awards='100')


session = Session()     #建立到数据库的会话连接
session.add(sal1)
# session.add_all([bob,jack,tom,jane])         #真正向数据库写入记录
session.commit()
session.close()




