from django.contrib import admin
from .models import User, Category, Instrument, Like, Comment, UserProfile

admin.site.register({Category, Instrument, Like, Comment, UserProfile})
