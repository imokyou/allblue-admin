# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# 总的URL设置,新版本按下面的来不会有warning.
urlpatterns = [

    # 改成下面这种分APP的形式了.
    url(r'^$', include('app.snapshot.urls')),
    url(r'^user/', include('app.user.urls')),
    url(r'^api/user/', include('app.user.urls')),
    url(r'^group/', include('app.group.urls')),
    url(r'^api/group/', include('app.group.urls')),
]
