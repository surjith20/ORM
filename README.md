# Ex02 Django ORM Web Application
## Date: 27/09/2024

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
admin.py
from django.contrib import admin
from.models import Football_Player,Football_PlayerAdmin
admin.site.register(Football_Player,Football_PlayerAdmin)

model.py
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
```
## OUTPUT
![Screenshot (3)](https://github.com/user-attachments/assets/702beecf-8391-4153-a3cc-1e8828e21182)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
