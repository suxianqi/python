#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from Student import Session, Class, Stude

session = Session()
qurey1 = session.query(Class).order_by(Class.cla_num)
print(qurey1)
for name in qurey1:
    print(name)
    #########################################################3
qset1 = session.query(Stude.stu_phone, Stude.stu_name)
print(qset1)
for phone, name in qset1:
    print(phone, name)
##########################################################
qset2 = session.query(Stude.stu_name,Class.cla_name).join(Class,Class.cla_num ==Stude.stu_num)
print(qset2.all())
