#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from Student import Class,Session,Stude

# cla1=Class(cla_name='六年级(3)班',cla_num='1')
# cla2=Class(cla_name='六年级(4)班',cla_num='2')
# cla3=Class(cla_name='五年级(5)班',cla_num='3')

jony =Stude(stu_num='1',stu_name='Jony',cla_num='3',stu_phone='12345678')
jack =Stude(stu_num='2',stu_name='Jack',cla_num='1',stu_phone='98765441')
tom =Stude(stu_num='3',stu_name='Tom',cla_num='2',stu_phone='544677448')

session = Session()
session.add_all([jony,jack,tom])
session.commit()
session.close()



