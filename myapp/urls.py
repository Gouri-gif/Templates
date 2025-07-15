from django.contrib import admin
from django.urls import path,include
from .views import navbar,index

urlpatterns = [
    path('',index, name='index'),
    path('navbar/', navbar),
]