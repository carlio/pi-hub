from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pihub.proxy.views',
    url(r'^(?P<path>.+)$', 'get_path', name='get_path'),
    
)
