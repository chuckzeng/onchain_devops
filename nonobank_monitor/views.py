#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: ChuckZeng

from common.mymako import render_mako_context

def forms(request):
    """
    提交表格
    """
    return render_mako_context(request, '/forms.html')

def tables(request):
    """
    展示表格
    """
    return render_mako_context(request, '/tables.html')

def bootstrap(request):
    """
    bootstrap布局
    """
    return render_mako_context(request, '/bootstrap-grid.html')