#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from  django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$',views.polls_index, name='polls_index'),
]
