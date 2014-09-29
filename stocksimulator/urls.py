from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stocksimulator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'stock_app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stockapp/', include('stock_app.urls')),
)
