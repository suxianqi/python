#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#访问达内密码自动输入,浏览其他的页面共用cookie值

import urllib.request, urllib.parse, urllib.error
import http.cookiejar

cookie_filename = 'cookie.txt'
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

def get_cookie(LOGIN_URL,user_pass):
    postdata = urllib.parse.urlencode(user_pass).encode()
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)                 #全局的一个声明

    request = urllib.request.Request(LOGIN_URL, postdata, headers)
    try:
        response = opener.open(request)
        page = response.read().decode()
        # print(page)
    except urllib.error.URLError as e:
        print(e.code, ':', e.reason)

    cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中

if __name__ == '__main__':
    #需要修改的
    LOGIN_URL = 'http://uc.tmooc.cn/login/jumpTologin'
    password = input('input you password:')
    user_pass = {'user': '770219891@qq.com', 'password': password} # , 'submit' : 'Login'
    get_cookie(LOGIN_URL,user_pass)
    #固定的写法
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    cookie.load(cookie_filename, ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    #可以按需求改动的
    get_url = 'http://tts.tmooc.cn/studentCenter/toMyttsPage'  # 利用cookie请求訪问还有一个网址
    get_request = urllib.request.Request(get_url, headers=headers)
    get_response = opener.open(get_request)
    print(get_response.read().decode())










