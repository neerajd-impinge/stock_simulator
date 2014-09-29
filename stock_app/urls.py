from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
urlpatterns = patterns('',
    url(r'^signup/', 'stock_app.views.auth'),
    url(r'^login/', login,{'template_name':'login.html'}),
    url(r'^$', 'stock_app.views.home', name='home'),
)
