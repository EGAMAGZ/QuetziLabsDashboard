from django.urls import path

from .views import login,register,home,contact

urlpatterns=[
    path('login/',login,name="login"),
    path('register/',register,name="register"),
    path('contact/',contact,name="contact"),
    path('',home,name="home-page"),
]