from django.shortcuts import render

from .security import token_validation

# Create your views here.
# @token_validation
def home(request):
    return render(request,'home/home.html')