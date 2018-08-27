#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import String, Integer, Date, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker  # 创建ORM所需要的基类

engine = create_engine(
    'mysql+pymysql://root:123456@127.0.0.1/student?charset=utf8',
    encoding='utf8'
)
Base = declarative_base()  # 创建ORM所需的基类
Session = sessionmaker(bind=engine)


class Class(Base):
    __tablename__ = 'class'
    cla_name = Column(String(40), nullable=False)
    cla_num = Column(Integer, primary_key=True)

    def __str__(self):
        return '[%s:%s]' % (self.cla_name, self.cla_num)


class Stude(Base):
    __tablename__ = 'students'

    stu_num = Column(Integer,primary_key=True)   #不加primary_key报错
    stu_name = Column(String(10), nullable=False)
    cla_num = Column(Integer, ForeignKey('class.cla_num'))
    stu_phone = Column(String(11),nullable=False)

    def __str__(self):
        return '[%s:%s]' %(self.stu_name ,self.stu_num)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
