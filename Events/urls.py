from django.urls import path 
from .views import *   

urlpatterns = [
    path('', EventList.as_view(), name='view_classes'),
    path('filter',EventFilter.as_view(), name="Filter Event"),
    path('search',EventSearch.as_view(), name="search Event"),
    path('detail/<int:pk>', EventDetail.as_view(),name='view_details'),
]