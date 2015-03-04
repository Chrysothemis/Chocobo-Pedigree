from django.conf.urls import patterns, include, url
from django.contrib import admin
from choco.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'choco.views.index', name='home'),
    url(r'^chocobo/(?P<chocobo_id>\d+)', 'choco.views.choco_page', name='choco_page'),
    url(r'^user/(?P<user_id>\d+)', 'choco.views.user_page', name='user_page'),
    #url(r'^$', 'index', name='index'),
    url(r'^logout/', 'choco.views.logout_view', name='logout'),
    url(r'^login/', 'choco.views.login_view', name='login'),
    url(r'^register/', 'choco.views.register', name='register'),
    url(r'register_view/', 'choco.views.register_view', name='register_view'),
    url(r'^new_choco/', 'choco.views.new_choco', name='new_choco'),
    url(r'new_choco_view/', 'choco.views.new_choco_view', name='new_choco_view'),
)
