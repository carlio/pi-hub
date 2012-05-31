from django.shortcuts import get_object_or_404
from pihub.packages.models import Pkg
from annoying.decorators import render_to


@render_to('packages/simple/package_detail.html')
def package_detail(request, package_name):
    pkg = get_object_or_404(Pkg, name=package_name)
    return {'pkg': pkg, 'releases': pkg.release_set.all() }

@render_to('packages/simple/index.html')
def package_index(request):
    return { 'packages': Pkg.objects.all() }