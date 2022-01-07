from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import * 

class ProjectView(viewsets.ModelViewSet):
	serializer_class = ProjectSerializer
	queryset = Project.objects.all() 