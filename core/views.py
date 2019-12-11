from django.shortcuts import render
from django.http import HttpResponseRedirect

from .form import LoginForm

# Create your views here.
def homeRoot(request):
    if(request.method=="POST"):
        form=LoginForm(request.POST)
        return HttpResponseRedirect('/home')
    else:
        form=LoginForm()
    return render(request,'core/main_template.html',{'form':form})