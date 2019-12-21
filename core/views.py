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
            return HttpResponseRedirect('/home')
    else:
        form=LoginForm()
    return render(request,'core/login.html',{'form':form})

@csrf_protect
@xframe_options_deny
def register(request):
    return render(request,'core/register.html')

@csrf_protect
@xframe_options_deny
def contact(request):
    return render(request,'core/contact.html')