from django.shortcuts import render

# Create your views here.
def homeRoot(request):
    return render(request,'core/main_template.html')