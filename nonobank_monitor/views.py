#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: ChuckZeng

from common.mymako import render_mako_context

def form(request):
    """
    首页
    """
    return render_mako_context(request, '/form.html')
