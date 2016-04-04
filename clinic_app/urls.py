from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import *

urlpatterns = [
    url(r'^$', ListNews.as_view(), name='home-page')
]
urlpatterns += staticfiles_urlpatterns()