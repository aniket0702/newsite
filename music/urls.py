from django.conf.urls import url,include
from django.contrib import admin
from . import views
app_name = 'music'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
]
