from annoying.decorators import render_to
from pihub.packages.models import Pkg, Release

@render_to('index.html')
def site_index(request):
    return { 'package_count': Pkg.objects.all().count(),
             'release_count': Release.objects.all().count(),
             'private_package_count': Pkg.objects.filter(private=True).count(),
             'private_release_count': Release.objects.filter(pkg__private=True).count() }