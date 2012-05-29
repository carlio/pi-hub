from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pihub.packages.views',
    url(r'^(?P<package_name>[a-zA-Z0-9-]+)$', 'version_list', name='version_list'),
    
    url(r'^packages/source/\w/\w+/(\w+.tar.gz)#md5=bff9fc7d871c0b5e6ce1a7babd16847b', 'tarball', name='tarball'),
    
)
