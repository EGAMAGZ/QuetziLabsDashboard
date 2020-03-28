from django.shortcuts import render

from home.security import token_validation
# Create your views here.
@token_validation('/login/')
def home(request):
    return render(request,'home/home.html')