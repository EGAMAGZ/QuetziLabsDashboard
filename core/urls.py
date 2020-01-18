from django.urls import path

from .views import login,register,home,contact,logout

urlpatterns=[
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
    path('register/',register,name="register"),
    path('contact/',contact,name="contact"),
    path('',home,name="home-page"),
]