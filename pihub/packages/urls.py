from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pihub.packages.simple_views',
    url(r'^simple/$', 'package_index', name='simple_index'),
    url(r'^simple/(?P<package_name>.*[^/])/?$', 'package_detail', name='simple_detail'),
)

urlpatterns += patterns('pihub.packages.views',
    url(r'^download/(?P<package_name>.+)/(?P<file_name>.+)$', 'download', name='download'),    
    url(r'^(?P<package_name>.+)/$', 'package_detail', name='package_detail'),
    url(r'^search$', 'search', name='search'),
    
    url(r'^(?P<package_name>.+)/(?P<version>.+)$', 'release_detail', name='release_detail'),
)
