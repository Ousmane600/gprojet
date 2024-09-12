from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

def login_view(request):
   return render(request, 'login.html')

def profil_view(request):
   return render(request, 'profil.html')

def sigup_view(request):
   return render(request, 'sigup.html')

