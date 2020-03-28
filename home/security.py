from django.http import HttpResponseRedirect

from core.models import Freelancer_Data
from qtz_tools.jwtConfig import JWTtool

class token_validation:
    def __init__(self,path):
        self.path=path

    def __call__(self,func):
        def wrapper(request,*args,**kwargs):
            try:
                jwt=JWTtool()
                token=request.session['qtz-session']
                if(jwt.is_valid(token)):
                    return func(request,*args,**kwargs)
                else:
                    return HttpResponseRedirect('/login/')
            except (KeyError,Freelancer_Data.DoesNotExist):
                return HttpResponseRedirect('/login/')
        return wrapper
