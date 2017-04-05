from django.contrib import admin
from .models import User, Category, Instrument, Like, Comment

admin.site.register({Category, Instrument, Like, Comment})
