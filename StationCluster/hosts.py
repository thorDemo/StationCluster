from django_hosts import patterns, host
from django.conf import settings
from CPModel_1 import views
from CPModel_2 import views
from CPModel_3 import views

host_patterns = patterns('',
    host(r'^api', 'CPModel_1.urls', name='api'),
    host(r'^beta', 'CPModel_2.urls', name='beta'),
)