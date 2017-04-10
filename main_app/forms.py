from django import forms
from .models import User, Category, Instrument, Like, Comment
from django.core.exceptions import ObjectDoesNotExist

class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = {'name', 'category', 'address', 'price', 'image', 'video', 'content'} 


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())


class CreateAccountForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

    def checkUserName(username):
        try:
            user = User.objects.get(username= username)
        except ObjectDoesNotExist:
            user = None
        if (user == None):
            return False


