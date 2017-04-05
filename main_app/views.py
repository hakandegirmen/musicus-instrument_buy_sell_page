from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Category, Instrument, Like, Comment
from .forms import InstrumentForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    instruments = Instrument.objects.all()
    form = InstrumentForm()
    return render(request, 'index.html', {'instruments': instruments, 'form': form })
    
# Create your views here.



