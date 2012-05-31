from pihub.manager import get_binary
from django.http import HttpResponse
from pihub.packages.models import Pkg, ReleaseUrl
from django.shortcuts import get_object_or_404

# taken from:
# http://metalinguist.wordpress.com/2008/02/12/django-file-and-stream-serving-performance-gotcha/

class FileIterWrapper(object):
    def __init__(self, flo, chunk_size=1024 ** 2):
        self.flo = flo
        self.chunk_size = chunk_size

    def next(self):
        data = self.flo.read(self.chunk_size)
        if data:
            return data
        else:
            raise StopIteration

    def __iter__(self):
        return self


def download(request, package_name, file_name):
    
    pkg = get_object_or_404(Pkg, name=package_name)
    release_url = get_object_or_404(ReleaseUrl, filename=file_name, release__pkg=pkg)
    
    filepath = get_binary(release_url)
    
    return HttpResponse(FileIterWrapper(open(filepath)))    
