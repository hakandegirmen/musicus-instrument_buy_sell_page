from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from address.models import AddressField

class category(models.Model):
    
    name = models.CharField(max_length=100)
    code_name = models.CharField(max_length=100)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateField(blank=True, null=True)
    deleted = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class instrument(models.Model):
    
    user = models.ForeignKey(User)
    category = models.ForeignKey(category, on_delete=models.CASCADE, default = 'unknown')

    name = models.CharField(max_length=100)
    address = AddressField(blank=True, null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image_files', default='media/default.png')
    video = models.URLField(max_length=200, blank=True, null=True)
    number_of_likes = models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateField(blank=True, null=True)
    deleted = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class like(models.Model):
    
    user = models.ForeignKey(User)
    instrument = models.ForeignKey(instrument, on_delete=models.CASCADE)
    
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateField(blank=True, null=True)
    deleted = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class comment(models.Model):
    
    user = models.ForeignKey(User)
    instrument = models.ForeignKey(instrument, on_delete=models.CASCADE)
    ref_self = models.ForeignKey('self')

    created = models.DateTimeField(default=datetime.now)
    updated = models.DateField(blank=True, null=True)
    deleted = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    

    def __str__(self):
        return self.name