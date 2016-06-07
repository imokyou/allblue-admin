# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponse
from . import permissions


def HttpRender(request, template, data={}):
    menus = permissions.get_user_menu(request)
    data['menus'] = menus
    return render(request, template, data)


def HttpJsonResponse(data):
    return HttpResponse(json.dumps(data), content_type='application/json')


def NormalResp(d={}):
    data = {'c': 0, 'm': '', 'd': d}
    return HttpResponse(json.dumps(data), content_type='application/json')
