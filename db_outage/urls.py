from django.conf import settings
from django.conf.urls import patterns, include, url
from db_outage.views import DBOutage

try:
    outage_url = settings.OUTAGE_URL
except AttributeError:
    outage_url = r'^outage/$'

urlpatterns = patterns('',
    url(outage_url, DBOutage.as_view(), name='db_outage',),
)
