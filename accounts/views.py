from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_api(request):
  return render(request, 'accounts/home.html')
  