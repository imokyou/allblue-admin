# -*- coding: utf-8 -*-
MENUS = [
    {
        'has_submenu': False,
        'name': 'Dashboard',
        'uri': '/',
        'icon': 'zmdi zmdi-view-dashboard',
        'active': False,
        'class': '',
        'submenu': []
    },
    {
        'has_submenu': True,
        'name': '后台管理模块',
        'uri': '#',
        'icon': 'fa fa-cog',
        'active': False,
        'submenu': [
            [
                {
                    'name': '权限组列表',
                    'uri': '/group/list/',
                    'icon': '',
                    'active': False,
                    'class': '',
                },
                {
                    'name': '管理账号列表',
                    'uri': '/user/list/',
                    'icon': '',
                    'active': False,
                },
            ]
        ]
    },
    {
        'has_submenu': True,
        'name': '媒介管理',
        'uri': '#',
        'icon': 'zmdi zmdi-view-dashboard',
        'active': False,
        'submenu': [
            [
                {
                    'name': '应用列表',
                    'uri': '/application/list/',
                    'icon': '',
                    'active': False,
                },
            ]
        ]
    },
]


def get_user_menu(request):
    current_uri = request.META['REQUEST_URI'].split('?')[0].split('/')
    urilist = [x for x in current_uri if x]
    if not urilist:
        current_uri = '/'
    else:
        current_uri = '/%s/' % '/'.join(urilist)
    for menu in MENUS:
        menu['active'] = False
        if menu['has_submenu']:
            for submenu in menu['submenu']:
                for m in submenu:
                    m['active'] = False
                    if m['uri'] == current_uri:
                        m['active'] = True
                        menu['active'] = True
        else:
            if menu['uri'] == current_uri:
                menu['active'] = True
    return MENUS
