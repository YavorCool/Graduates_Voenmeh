from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.views import static

from Graduates_Voenmeh import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('graduates.urls')),

]