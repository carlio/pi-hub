import re
from django.shortcuts import redirect

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
        uses_proxy = any( [ua.match(user_agent) for ua in _USER_AGENTS] )
        
        if uses_proxy and not request.path.startswith('/proxy'):
            return redirect( '/proxy' + request.path )
    
