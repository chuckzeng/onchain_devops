#! /usr/bin/env python
# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
# from django.shortcuts import render
from navi import models
from forms import navi_form

# Create your views here.

def index(request):
    temp_name = "navi/navi-header.html"
    allnavi = models.navi.objects.all()
    return render_mako_context(request, "navi/index.html", locals())

def add(request):
    # temp_name = "navi/navi-header.html"
    if request.method == "POST":
        n_form = navi_form(request.POST)
        if n_form.is_valid():
            n_form.save()
            tips = u"增加成功！"
            display_control = ""
        else:
            tips = u"增加失败！"
            display_control = ""
        return render_mako_context(request, "navi/add.html", locals())
    else:
        display_control = "none"
        tips = "none"
        n_form = navi_form()
        return render_mako_context(request, "navi/add.html", {"display_control":display_control,"n_form":n_form,
                                                              "tips":tips},)

def manage(request):
    allnavi = models.navi.objects.all()
    return render_mako_context(request, "navi/manage.html", locals())