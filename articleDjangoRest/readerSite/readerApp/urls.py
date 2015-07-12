#!/usr/bin/env python
from django.conf.urls import include, url
import views


urlpatterns=[
    url(r'^(?P<article_id>[0-9]+)/$', views.articlePage, name='title'),
    url(r'search',views.searchResults, name ='views'),
    url(r'landing',views.landingPage, name ='views'),
]

