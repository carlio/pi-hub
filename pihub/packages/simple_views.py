from django.shortcuts import get_object_or_404, redirect
from pihub.packages.models import Pkg, FetchStatus
from annoying.decorators import render_to
from django.http import HttpResponse


@render_to('packages/simple/package_detail.html')
def package_detail(request, package_name):
    pkg = get_object_or_404(Pkg, name__iexact=package_name)
    if pkg.name != package_name:
        # the official capitalisation is different, but easy_install / pip
        # should be case agnostic. in this situation, we redirect to the 
        # correct package name
        return redirect('packages:simple_detail', pkg.name)

    if pkg.fetch_status != FetchStatus.COMPLETE:
        return HttpResponse('hello')
    
    return {'pkg': pkg, 'releases': pkg.release_set.all() }

@render_to('packages/simple/index.html')
def package_index(request):
    return { 'packages': Pkg.objects.all() }