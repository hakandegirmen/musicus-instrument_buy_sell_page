from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from address.models import AddressField

class Category(models.Model):
    
    #properties
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    
    #record info
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateField(blank=True, null=True)
    deleted = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Instrument(models.Model):
    
    #foreign keys
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    #properties
    name = models.CharField(max_length=100)
    address = AddressField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='image_files', default='media/default.png')
    video = models.URLField(max_length=200, blank=True, null=True)
    number_of_likes = models.IntegerField(default=0)
    content = models.TextField(blank=True, null=True)
    
    #record info
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateField(blank=True, null=True)
    deleted = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Like(models.Model):
    
    #foreign keys
    user = models.ForeignKey(User)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    
    #record info
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateField(blank=True, null=True)
    deleted = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    
    #foreign keys
    user = models.ForeignKey(User)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    ref_self = models.ForeignKey('self', blank=True, null=True)

    #properties
    content = models.TextField(blank=True, null=True)

    #record info
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateField(blank=True, null=True)
    deleted = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)