from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Category, Instrument, Like, Comment, UserProfile
from .forms import InstrumentForm, LoginForm, CreateAccountForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    instruments = Instrument.objects.all()
    form = InstrumentForm()
    return render(request, 'index.html', {'instruments': instruments, 'form': form })
  
def detail(request, instrument_id):
    instrument = get_object_or_404(Instrument, id=instrument_id)
    comments= Comment.objects.all()
    userProfiles = UserProfile.objects.all()

    return render(request, 'detail.html', {
        'instrument': instrument,
        'comments': comments,
        'userProfiles': userProfiles
    })
  
def post_instrument(request):

    form = InstrumentForm(request.POST, request.FILES)
    if form.is_valid():
        instrument = form.save(commit= False)
        instrument.user = request.user
        instrument.save()

    return HttpResponseRedirect('/')


def profile(request, username):
    user = User.objects.get(username = username)
    instruments = Instrument.objects.filter(user = user)
    return render(request, 'profile.html',
                  {'instruments': instruments,
                   'username': username })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled")
                    #Code to render disabled user error HTML
            else:
                print("Incorrect username or password")
                # Code to render incorrect entry error HTML

    else:
        form = LoginForm()
        return render(request, 'login.html',
                      {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def create_account(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = form.save()





