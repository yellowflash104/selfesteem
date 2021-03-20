from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def welcome(request):
	return render(request,'app/welcome.html')

def home(request):
	return render(request,'app/home.html')
