#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: ChuckZeng


from nonobank_monitor import views
from django.conf.urls import url


urlpatterns = [
    url(r'^form$', views.form),
]