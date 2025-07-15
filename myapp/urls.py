from django.contrib import admin
from django.urls import path,include
from .views import navbar, home ,index

urlpatterns = [
    path('',index, name='index'),
    path('navbar/', navbar),
    path('home/',home,name='home')  # Include URLs from myapp
]