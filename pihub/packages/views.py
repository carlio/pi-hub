from pihub.manager import get_binary_path
from pihub.packages.models import Pkg, ReleaseUrl
from django.shortcuts import get_object_or_404
from django.views.static import serve


def download(request, package_name, file_name):
    
    pkg = get_object_or_404(Pkg, name=package_name)
    release_url = get_object_or_404(ReleaseUrl, filename=file_name, release__pkg=pkg)
    
    filepath = get_binary_path(release_url)
    return serve(request, filepath, '/')
