from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.views.decorators.clickjacking import xframe_options_deny
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .form import LoginForm

# Create your views here.
@csrf_exempt
def home(request):
    return render(request,'core/home.html')

@csrf_protect
@xframe_options_deny
def login(request):
    if(request.method=="POST"):
        form=LoginForm(request.POST)
        if(form.is_valid()):
            if(form.cleaned_data['ad_remember']):
                request.session['qtz-email-storage']=form.cleaned_data['ad_email']
                request.session['qtz-remember-storage']=form.cleaned_data['ad_remember']
            else:
                request.session['qtz-email-storage']=None
                request.session['qtz-remember-storage']=None
            return HttpResponseRedirect('/home')
    else:
        try:
            ad_email=request.session['qtz-email-storage']
            ad_remember=request.session['qtz-remember-storage']
        except:
            ad_email=""
            ad_remember=False
        form=LoginForm(initial={'ad_email':ad_email,'ad_remember':ad_remember})
    # from django.conf import settings
    # print(settings.COUNTRIES_CODE)
    return render(request,'core/login.html',{'form':form})

@csrf_protect
@xframe_options_deny
def register(request):
    return render(request,'core/register.html')

@csrf_protect
@xframe_options_deny
def contact(request):
    return render(request,'core/contact.html')