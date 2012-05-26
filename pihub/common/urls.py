from django.conf.urls.defaults import patterns, url
from django.views.generic.base import TemplateView

urlpatterns = patterns('boobdb.common.views',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='site_index'),
)
