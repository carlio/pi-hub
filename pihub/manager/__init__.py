

from django.conf import settings
import os
from django.template.defaultfilters import slugify
from urlparse import urljoin
import urllib2


class NotFound(Exception):
    pass


def get_binary(release_url):
    
    pkg = release_url.release.pkg
    pkg_dir = slugify(pkg.name)
    
    if pkg.private:
        # if this is a custom package, check our local directory
        local_dir = os.path.join(settings.PACKAGE_DIRECTORY, 'local')
        filepath = os.path.join(local_dir, pkg_dir, release_url.filename )
        if os.path.exists(filepath):
            return filepath
        raise NotFound
    else:
        # see if we have already cached it
        cache_dir = os.path.join(settings.PACKAGE_DIRECTORY, 'cache')
        filepath = os.path.join(local_dir, pkg_dir, release_url.filename )
        if os.path.exists(filepath):
            return filepath
        
        # now check PyPI
        # TODO: this is very naive URL fetching
        url = urljoin('http://pypi.python.org/simple/', pkg.name, release_url.filename)
        contents = urllib2.urlopen(url).read()
        os.makedirs( os.path.join(cache_dir, pkg_dir ) )
        with open( filepath, 'w') as f:
            f.write(contents)
    
        return filepath
