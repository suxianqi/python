#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello World</h1>')
