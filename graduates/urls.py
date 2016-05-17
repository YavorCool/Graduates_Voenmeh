from django.conf.urls import url, include, patterns
from django.contrib import admin

from graduates import views

urlpatterns = [
     url(r'^$', views.graduates),
     url(r'^search/$', views.search_surname),
     url(r'^search_faculty/$', views.search_faculty),
     url(r'^specs_by_faculty/$', views.specs_by_faculty),
     url(r'^search_speciality/$', views.search_speciality),
     url(r'^groups_by_faculty/$', views.groups_by_faculty),
     url(r'^get_graduate_description/(?P<id>\d+)$', views.get_graduate_description),
     url(r'^get_faculty_description/(?P<id>\d+)$', views.get_faculty_description),
     url(r'^get_kaf_description/(?P<id>\d+)$', views.get_kaf_description),
     url(r'^search_by_group/$', views.filter_by_group),
     url(r'^spec_list_by_group/$', views.spec_list_by_group),
     url(r'^group_list_by_spec/$', views.group_list_by_spec),
]