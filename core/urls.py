from django.urls import path

from .views import homeRoot

urlpatterns=[
    path('',homeRoot)
]