#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from http import cookiejar
from  urllib import request
import urllib.parse
from bs4 import BeautifulSoup

def saveCookie(LOGIN_URL,**kwargs,):
    adict = kwargs
    filename = 'cookie.txt'
    LOGIN_URL = 'http://uc.tmooc.cn/login/jumpTologin'
    postdata = urllib.parse.urlencode(values).encode()
    user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

    cookie = cookiejar.MozillaCookieJar(filename)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('https://www.zhihu.com/question/25313930')
    # ignore_discard的意思是即使cookies将被丢弃也将它保存下来；
    # ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
    cookie.save(ignore_discard=True, ignore_expires=True)



if __name__ == '__main__':
    values = {'user': '770219891@qq.com', 'password': 'SUxianqi1'}  # , 'submit' : 'Login'
    saveCookie()
