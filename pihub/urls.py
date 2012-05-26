from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # catchall for anything unmatched goes into the common app
    url(r'', include('pihub.common.urls')),
)

from django.conf import settings
if settings.DEBUG:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns += patterns('', url(r'^admin/', include(admin.site.urls)),)

