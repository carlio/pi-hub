from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pihub.common.views',
    url(r'^$', 'site_index', name='site_index'),
    
    url(r'^fetchstatus/index$', 'fetch_status_index', name='fetch_status_index'),
)
