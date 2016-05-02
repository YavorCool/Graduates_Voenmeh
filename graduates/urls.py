from django.conf.urls import url, include, patterns
from django.contrib import admin

from graduates import views

urlpatterns = [
     url(r'^$', views.graduates),
     url(r'^search/$', views.search_surname),
     url(r'^search_faculty/$', views.search_faculty),
     url(r'^search_speciality/$', views.search_speciality),
     url(r'^get_graduate_description/(?P<id>\d+)$', views.get_graduate_description),
]