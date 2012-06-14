from annoying.decorators import render_to, ajax_request
from pihub.packages.models import Pkg, Release, get_mirror_state

@render_to('index.html')
def site_index(request):
    return { 'package_count': Pkg.objects.all().count(),
             'release_count': Release.objects.all().count(),
             'private_package_count': Pkg.objects.filter(private=True).count(),
             'private_release_count': Release.objects.filter(pkg__private=True).count() }
    
    
@ajax_request
def fetch_status_index(request):
    return {'fetched': get_mirror_state().index_fetched}