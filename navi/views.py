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

def delete(request):
    if request.method == 'POST':
        navi_items = request.POST.getlist('navi_check', [])
        if navi_items:
            for n in navi_items:
                models.navi.objects.filter(id=n).delete()
    allnavi = models.navi.objects.all()
    return render_mako_context(request, "navi/manage.html", locals())

def edit(request):
    if request.method == 'GET':
        item = request.GET.get("id")
        obj = models.navi.objects.get(id=item)
    return render_mako_context(request, "navi/edit.html", locals())

def save(request):
    if request.method == 'POST':
        ids = request.POST.get('id')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        url = request.POST.get('url')
        navi_item = models.navi.objects.get(id=ids)
        navi_item.name = name
        navi_item.description = desc
        navi_item.url = url
        try:
            navi_item.save()
            status = "1"
        except AttributeError,e:
            print e.message
    else:
        status = "2"
    allnavi = models.navi.objects.all()
    # print status
    return render_mako_context(request, "navi/edit.html", locals())