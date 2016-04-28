from django.conf.urls import url, include, patterns
from django.contrib import admin

from graduates import views

urlpatterns = [
     url(r'^$', views.graduates),
     url(r'^main/(?P<mode>\w+)/(?P<page_number>\d+)$', views.graduates),
     url(r'^search/$', views.search_surname),
     url(r'^search_faculty/$', views.search_faculty),
     url(r'^search_speciality/$', views.search_speciality),
]