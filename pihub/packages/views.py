from annoying.decorators import render_to
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe
from django.views.static import serve
from docutils.core import publish_parts
from pihub.manager import get_binary_path
from pihub.packages.models import Pkg, ReleaseUrl, Release, ReleaseData


def download(request, package_name, file_name):
    
    pkg = get_object_or_404(Pkg, name=package_name)
    release_url = get_object_or_404(ReleaseUrl, filename=file_name, release__pkg=pkg)
    
    filepath = get_binary_path(release_url)
    return serve(request, filepath, '/')


@render_to('packages/detail.html')
def package_detail(request, package_name):
    
    pkg = get_object_or_404(Pkg, name=package_name)
    release_datas = ReleaseData.objects.filter(release__pkg=pkg)
    return { 'pkg': pkg, 'release_datas': release_datas }


_LICENSE_URLS = {'BSD': 'http://en.wikipedia.org/wiki/BSD_licenses',
                 }


@render_to('packages/release_detail.html')
def release_detail(request, package_name, version):
    
    pkg = get_object_or_404(Pkg, name=package_name)
    release = get_object_or_404(Release, pkg=pkg, version=version)
    
    release_data = get_object_or_404(ReleaseData, release=release)
    release_urls = release.releaseurl_set.all()
    
    license_url = _LICENSE_URLS.get(release_data.license, '')
    
    settings_overrides = {
        'raw_enabled': 0,  # no raw HTML code
        'file_insertion_enabled': 0,  # no file/URL access
        'halt_level': 2,  # at warnings or errors, raise an exception
        'report_level': 5,  # never report problems with the reST code
    }

    try:
        parts = publish_parts(source=release_data.description,
                              writer_name='html',
                              settings_overrides=settings_overrides)
        description = parts['body']
    except:
        description = '<pre>%s</pre>' % release_data.description
    
    description = mark_safe(description)
    
    
    return { 'pkg': pkg, 'release': release, 
             'release_data': release_data,
             'license_url': license_url,
             'release_urls': release_urls,
             'description': description }


@render_to('packages/search.html')
def search(request):
    if 't' not in request.GET:
        return {}
    
    term = request.GET['t']
    results = Pkg.objects.filter(name__icontains=term)
        
    # TODO: add haystack for full text searching of other attributes
    return {'results': results}
        
