from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.views.decorators.clickjacking import xframe_options_deny
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password

from .form import LoginForm,RegisterForm
from .models import QL_FREE_DT
from qtz_tools.jwtConfig import JWTtool

# Create your views here.
@csrf_exempt
def home(request):
    return render(request,'core/home.html')

@csrf_protect
@xframe_options_deny
def login(request):
    custom_errors={}
    if(request.method=="POST"):
        form=LoginForm(request.POST)
        if(form.is_valid()):
            jwt=JWTtool()
            if(form.cleaned_data['ad_remember']):
                request.session['qtz-email-storage']=form.cleaned_data['ad_email']
                request.session['qtz-remember-storage']=form.cleaned_data['ad_remember']
            else:
                request.session['qtz-email-storage']=None
                request.session['qtz-remember-storage']=None
            try:
                db_model=QL_FREE_DT.objects.get(ql_free_email=form.cleaned_data['ad_email'])
                print(db_model.ql_free_img_link)
                if(check_password(form.cleaned_data['ad_password'],db_model.ql_free_pass)):
                    return HttpResponseRedirect('/home')
                else:
                    custom_errors['password_error']="Cuenta o contraseña incorrectos"
            except QL_FREE_DT.DoesNotExist:
                custom_errors['login_error']="Esta cuenta no existe"
    else:
        try:
            ad_email=request.session['qtz-email-storage']
            ad_remember=request.session['qtz-remember-storage']
        except:
            ad_email=""
            ad_remember=False
        form=LoginForm(initial={'ad_email':ad_email,'ad_remember':ad_remember})
    return render(request,'core/login.html',{'form':form,'custom_errors':custom_errors})

@csrf_protect
@xframe_options_deny
def register(request):
    custom_errors={}
    if(request.method=="POST"):
        form=RegisterForm(request.POST,request.FILES)
        if(form.is_valid()):
            if(form.cleaned_data['ad_password'] == form.cleaned_data['ad_password_s']):
                request.session['qtz-email-storage']=form.cleaned_data['ad_email']
                request.session['qtz-remember-storage']=True
                db_model=QL_FREE_DT(ql_free_img_link=form.cleaned_data['ad_profile'],ql_free_name=form.cleaned_data['ad_name'],
                    ql_free_email=form.cleaned_data['ad_email'],ql_free_pass=make_password(form.cleaned_data['ad_password']),
                    ql_free_username=form.cleaned_data['ad_username'],ql_free_gender=form.cleaned_data['ad_genre'])
                db_model.save()
                return HttpResponseRedirect('/login')
            else:
                custom_errors['dif-passwords']="Contraseñas no coinciden"
        print(form.cleaned_data)
    else:
        form=RegisterForm()
    return render(request,'core/register.html',{'form':form,'custom_errors':custom_errors})

@csrf_protect
@xframe_options_deny
def contact(request):
    return render(request,'core/contact.html')