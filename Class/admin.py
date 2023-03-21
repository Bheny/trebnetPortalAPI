from django.contrib import admin
from Profiles.models import ClassApplication
from .models import Class 

admin.site.register(ClassApplication)
admin.site.register(Class)
