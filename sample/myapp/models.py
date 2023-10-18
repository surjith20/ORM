from django.db import models
from django.contrib import admin
class Football_Player (models.Model):
    name=models.CharField(max_length=120)
    age=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    doj=models.DateField()
    email=models.EmailField()
class Football_PlayerAdmin(admin.ModelAdmin):
    list_display=('name','age','phone_number','doj','email')
