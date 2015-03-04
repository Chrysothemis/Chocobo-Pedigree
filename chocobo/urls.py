from django.conf.urls import patterns, include, url
from django.contrib import admin
from choco.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'choco.views.index', name='home'),
    url(r'^chocobo/(?P<chocobo_id>\d+)', 'choco.views.choco_page', name='choco_page'),
    #url(r'^$', 'index', name='index'),
)
