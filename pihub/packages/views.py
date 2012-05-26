
import os
from django.conf import settings
from django.http import Http404, HttpResponse
import urllib2
from urlparse import urljoin


def _get_file(package_name, version=None):
    
    specific_file = version or 'index.html'

    local_dir = os.path.join(settings.PACKAGE_DIRECTORY, 'local')
    cache_dir = os.path.join(settings.PACKAGE_DIRECTORY, 'cache')
        
    # first check our local packages, then cached packages
    for directory in (local_dir, cache_dir):
        package_dir = os.path.join( directory, package_name )
        if os.path.exists(package_dir):
            # see if we have the specific file
            package_file = os.path.join( directory, package_name, specific_file )
            if os.path.exists:
                with open(package_file) as f:
                    return f.read()
        
    # now check PyPI
    # TODO: this is very naive URL fetching
    url = urljoin('http://pypi.python.org/simple/', package_name, specific_file)
    contents = urllib2.urlopen(url).read()
    os.makedirs( os.path.join(cache_dir, package_name ) )
    with open( os.path.join(cache_dir, package_name, specific_file), 'w') as f:
        f.write(contents)
    
    return contents


def version_list(request, package_name):
    # see if we already have an index.html page cached
    return HttpResponse( _get_file(package_name) )