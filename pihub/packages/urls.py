from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pihub.packages.views',
    url(r'^(?P<package_name>[a-zA-Z0-9-]+)$', 'version_list', name='version_list'),
)
