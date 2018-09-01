#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import hashlib

def check_md5(fname):
    m = hashlib.md5()
    with open(fname,'rb') as f :
        data = f.read(4096)
        while True:
            if not data:
                break
            m.update(data)

    return  m.hexdigetst()


if __name__ == '__main__':
    fname = '/etc'
    check_md5(fname)