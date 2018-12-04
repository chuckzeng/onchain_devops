#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: ChuckZeng

from django.conf.urls import url
from nonobank_monitor import views

urlpatterns = [
    url(r'^forms/', views.forms),
    url(r'^tables/', views.tables),
    url(r'^bootstrap/', views.bootstrap),
]