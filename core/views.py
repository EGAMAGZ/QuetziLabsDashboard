from django.shortcuts import render
from django.http import HttpResponseRedirect

from .form import LoginForm

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def login(request):
    if(request.method=="POST"):
        form=LoginForm(request.POST)
        if(form.is_valid()):
            return HttpResponseRedirect('/home')
    else:
        form=LoginForm()
    return render(request,'core/login.html',{'form':form})

def register(request):
    return render(request,'core/base.html')