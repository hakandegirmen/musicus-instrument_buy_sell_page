from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from .models import 
# from .forms import
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    
    return render(request, 'index.html')
    
# Create your views here.
