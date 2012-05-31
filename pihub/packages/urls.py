from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pihub.packages.simple_views',
    url(r'^simple/(?P<package_name>\w+)$', 'package_detail', name='simple_detail'),
)

urlpatterns += patterns('pihub.packages.views',
    url(r'^download/(?P<package_name>\w+)/(?P<file_name>.+)$', 'download', name='download'),
)
