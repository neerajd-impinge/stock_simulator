from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
urlpatterns = patterns('',
    url(r'^signup/', 'stock_app.views.auth'),
    url(r'^login/', login,{'template_name':'login.html'}),
	url(r'^search/', 'stock_app.views.search'),
	url(r'^view/(?P<company>.+?)/', 'stock_app.views.viewCompany', name="view_stock"),
	url(r'^stock/(?P<action>.+?)/', 'stock_app.views.stockAction', name="stock_action"),

)
