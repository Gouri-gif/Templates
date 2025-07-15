from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def navbar(request):
    return render(request, 'navbar.html')

def home(request):
    return render(request, 'home.html')