#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urllib import request
import requests
import os
import hashlib
import tarfile


def get_webdata(url):
    r = requests.get(url)  # 直接获取到网页的内容
    return r.text


def download(url, fname):
    html = request.urlopen(url)
    with  open(fname, 'wb')as f:
        while True:
            data = html.read(1024)
            if not data:
                break
            f.write(data)


def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()


def deploy(a_path):
    os.chdir('/var/www/html/deploy')
    tar = tarfile.open(a_path, 'r:gz')
    tar.extractall()
    tar.close()
    src = a_path.replace('.tar.gz', '')# 把后面的tar.gz去掉
    # src = src +'/index.html'
    dst = '/var/www/html/index.html'   #方便管理
    if os.path.exists(dst):
        os.unlink(dst)
    os.symlink(src,dst)

if __name__ == '__main__':
    ver = get_webdata('http://192.168.122.97:81/deploy/live_version').strip()
    app_name = 'test_v%s.tar.gz' % ver
    app_url = 'http://192.168.122.97:81/deploy/packages/' + app_name
    app_path = os.path.join('/var/www/html/deploy/', app_name)
    download(app_url, app_path)
    local_md5 = check_md5(app_path)
    remote_md5 = get_webdata(app_url + '.md5').strip()
    if local_md5 == remote_md5:
        deploy(app_path)
