# -*- coding: utf-8 -*-
from lib import utils


def test(request):
    pass


def page_list(request):
    return utils.HttpRender(request, 'application/list.html')
