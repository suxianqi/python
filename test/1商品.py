#!/usr/bin/env python
# -*- coding: UTF-8 -*-

choice = ['添加商品', '查找商品', '查看你所添加的商品', '退出']
li = ['电脑', '显示器', '笔记本', '机器键盘']
seruch = """0) 添加商品
1) 查找商品
2) 查看你所添加的商品
3) 退出
请输入(0/1/2/3): """

cat = """0) 电脑
1) 显示器
2) 笔记本
3) 机器键盘
请输入(0/1/2/3)： """
client_shop = []
exit = 0
while exit<3:
    ind = int(input(seruch))
    client = choice[ind]
    if client == choice[0]:
        client_add = input("输入添加的商品： ")
        print(type(client_add))
        client_shop.append(client_add)
    elif client == choice[1]:
        ind2 = int(input(cat))
        client2 = li[ind2]
        print('你查找的商品是： %s' % client2)
    elif client == choice[2]:
        print('你添加的商品有： %s' % client_shop)
    elif client == choice[3]:
        break
    else:
        print("请输入正确的选项")
        exit +=1