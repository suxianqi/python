#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from db_conn_sqlalchemy import Session, Departments, Salary, Employees

session = Session()  # order_by 排序
qset1 = session.query(Departments).order_by(Departments.dep_id)
print(qset1)

for dep in qset1:
    print(dep)

for dep in qset1:
    print('%s:%s' % (dep.dep_id, dep.dep_name))

#####################################################################
qset2 = session.query(Departments.dep_id, Departments.dep_name)
print(qset2)

for did, dname in qset2:
    print(did, dname)

##################################################################
qset3 = session.query(Departments)[2:5]
print(qset3)
for dep in qset3:
    print(dep.dep_name)
################################################################
qset4 = session.query(Departments.dep_name).filter(Departments.dep_id == 2)
print(qset4)  # 返回是sql语句
for dep in qset4:
    print(dep.dep_name)

###############################################################################
qset5 = session.query(  # 查询工资后相加
    Salary.date, Salary.emp_id, Salary.basic + Salary.awards
)
print(qset5)

for date, emp_id, sal in qset5:
    print('%s:%s:%s' % (date, emp_id, sal))

###############################################################################
qset6 = session.query(Departments.dep_id).filter(Departments.dep_name in ('Bob', 'Tom'))
print(qset6)  # 查询两个部门的ID
for did in qset6:
    print(did)

###################################################################################
qset7 = session.query(Departments.dep_id).filter(~Departments.dep_name.in_(['运维部', '开发部']))
print(qset7)  # 查询名字不是这两个部门的ID
for did in qset7:
    print(did)
################################################################################

from sqlalchemy import and_, or_

qset8 = session.query(Employees).filter(and_(Employees.gender == 'male', Employees.dep_id == 2))
print(qset8)  # 查询是男的和在2号部门的
for emp in qset8:
    print(emp.emp_name)
##################################################################################3
qset9 = session.query(Employees).filter(or_(Employees.gender == 'female', Employees.dep_id == 3))
print(qset9)  # 查询是女的或在3号部门的
for emp in qset9:
    print(emp.emp_name)

####################################################################################
qset10 = session.query(Departments).order_by(Departments.dep_id)
print(qset10.all())  # 返回查询集的列表,组成列表
print(qset10.first())  # 值返回查询到的第一个结果
# print(qset10.one())  #报错.one要求返回的结果只有一个
##############################################################################################
qset11 = session.query(Departments.dep_id, Departments.dep_name).filter(Departments.dep_id == 2)
print(qset11.one())
print(qset11.scalar())
######################################################################################
# 统计一共有几个部门
qset12 = session.query(Departments.dep_name).count()
print(qset12)
#################################################################3
# 得到每个员工在那个部门使用的名字,不用ID
qset13 = session.query(Employees.emp_name, Departments.dep_name).join(Departments,
             Employees.dep_id == Departments.dep_id)                     #********************  重点
print(qset13.all())  # 注意query()中先写Employees.emp_name,join()中就要先用Departments
##################################################################################
hr = session.query(Departments).filter(Departments.dep_name == 'hr')
print(hr)
hr.update({'dep_name': '人力资源部'})
session.commit()
session.close()
###############################################################################3
hr = session.query(Departments).get(1)
print(hr)
hr.dep_name = '人事部'
session.commit()
session.close()
######################################################################################
#删除id号为5的员工记录
ping = session.query(Employees).get(5)
session.delete(ping)
session.commit()
session.close()



