from django.conf.urls import url
import views

urlpatterns = [
    url(r'^test', views.test),
    url(r'^list', views.page_list),
]
