from django.shortcuts import get_object_or_404, redirect, render
from pihub.packages.models import Pkg, FetchStatus
from annoying.decorators import render_to
from django.http import HttpResponse
import requests
from pyquery import PyQuery as pq
from pihub.packages.tasks import fetch_releases_for_packages



def get_index_for_package(request, pkg):
    
    url = pkg.get_pypi_index()
    response = requests.get(url)
    
    doc = pq(response.text)
    
    files = []
    for anchor in doc('a'):
        a = pq(anchor)
        if a.attr('href').startswith('../../packages/'):
            # this is an actual package
            download_url = ''
            filename = a.text()
            files.append( (download_url, filename) )
    
    ctx = { 'pkg': pkg, 'files': files }
    return render(request, 'packages/simple/proxied_package_detail.html', ctx)

    

@render_to('packages/simple/package_detail.html')
def package_detail(request, package_name):
    pkg = get_object_or_404(Pkg, name__iexact=package_name)
    if pkg.name != package_name:
        # the official capitalisation is different, but easy_install / pip
        # should be case agnostic. in this situation, we redirect to the 
        # correct package name
        return redirect('packages:simple_detail', pkg.name)

    if pkg.fetch_status != FetchStatus.COMPLETE:
        # if we haven't scraped the content yet, then fetch it!
        fetch_releases_for_packages(Pkg.objects.filter(pk=pkg.id), async=False)
        pkg = Pkg.objects.get(pk=pkg.id)
    
    return {'pkg': pkg, 'releases': pkg.release_set.all() }

@render_to('packages/simple/index.html')
def package_index(request):
    return { 'packages': Pkg.objects.all() }