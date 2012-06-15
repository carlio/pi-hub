import re
from django.shortcuts import redirect, render
from pihub.packages.models import get_mirror_state, FetchStatus

# TODO: figure out Python3 user agent
_USER_AGENTS = map( re.compile, 
                        (
                         'Python-urllib/2.\d',                  # pip
                         'Python-urllib/2.\d setuptools/.*',    # easy_install
                        )
                  ) 


class RedirectSetuptools(object):
    
    def process_request(self, request):
        
        user_agent = request.META['HTTP_USER_AGENT']
        requires_simple = any( [ua.match(user_agent) for ua in _USER_AGENTS] )
        
        if requires_simple:
            if request.path.startswith('/packages/simple') or request.path.startswith('/packages/download'):
                return 
            return redirect( '/packages/simple' + request.path )
    


class WaitForIndexFetch(object):
    
    def process_request(self, request):
        if not any(map(request.path.startswith, ('/admin/', '/fetchstatus/'))):
            if get_mirror_state().index_fetch_status != FetchStatus.COMPLETE:
                return render(request, 'please_wait.html')