#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''MariaDB [tarena]> CREATE TABLE salary \                                   #PRIMARY 主键
    (auto_id INT AUTO_INCREMENT, date DATE, emp_id INT, basic INT, awards INT, PRIMARY KEY(auto_id),\
    FOREIGN KEY(emp_id) REFERENCES employees(emp_id));'''
# FOREIGN(外键)    #REFERENCES外键的值来值   employees是表名 后面那个表的那个字段名


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:123456@127.0.0.1/tarena?charset=utf8',
    encoding='utf8'  # echo=True debug的日志
)
####mysql+pymysql://用户名:@密码/库名?charset=utf8 #支持汉字

Base = declarative_base()  # 创建ORM所需要的基类

Session = sessionmaker(bind=engine)  # 绑定这个engine让后面方便用这个engine连接


class Departments(Base):
    __tablename__ = 'decpartments'  # 库中的表名
    dep_id = Column(Integer, primary_key=True)  # dep_id是表中的字段  默认是自增长primary_key = key
    dep_name = Column(String(20), unique=True)  # dep_那么是字符
    dep_years = Column(Integer)

    def __str__(self):
        return '[%s :%s]' % (self.dep_id, self.dep_name)


class Employees(Base):
    __tablename__ = 'employees'

    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20), nullable=False)
    gender = Column(String(6))
    birth_date = Column(Date)
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('decpartments.dep_id'))

    def __str__(self):
        return '[%s:%s]' % (self.emp_id, self.emp_name)


class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # 没有是创建,已经有不创建
