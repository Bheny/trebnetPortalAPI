from django.urls import path 
from .views import ClassList 

urlpatterns = [
    path('', ClassList.as_view(), name='view_classes'),
]