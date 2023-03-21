from django.urls import path 
from .views import *   

urlpatterns = [
    path('', ClassList.as_view(), name='view_classes'),
    path('detail/<int:pk>', ClassDetail.as_view(),name='view_details'),
    path('applications/', ClassApplicationList.as_view(), name='view_applications'),
    path('application/detail/<int:pk>', ClassApplicationDetail.as_view(), name="view_details")
]