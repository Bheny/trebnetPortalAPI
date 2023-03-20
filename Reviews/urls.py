from django.urls import path
from .views import ReviewList, ReviewDetail

urlpatterns = [
    path('', ReviewList.as_view(), name='view_Reviews'),
    path('detail/<int:pk>', ReviewDetail.as_view(), name='view_Reviews'),
   
]