from django.conf.urls import patterns, include, url
from db_outage.views import DBOutage

urlpatterns = patterns('',
    url(r'^outage/$', DBOutage.as_view(), name='db_outage',),
)
