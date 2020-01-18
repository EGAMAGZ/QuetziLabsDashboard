from django.http import HttpResponseRedirect

from core.models import QL_FREE_DT
from qtz_tools.jwtConfig import JWTtool

def token_validation(func):
    def func_wrapper(request,*args,**kwargs):
        try:
            jwt=JWTtool()
            token=request.session['qtz-session']
            if(jwt.is_valid(token)):
                return func(request,*args,**kwargs)
            else:
                return HttpResponseRedirect('/login/')
        except (KeyError,QL_FREE_DT.DoesNotExist):
            return HttpResponseRedirect('/login/')
