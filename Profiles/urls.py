from django.urls import path
from .views import ProfileList, ProfileDetail #, UpdateProfileDetail

urlpatterns = [
    path('', ProfileList.as_view(), name='view_profiles'),
    path('detail/<int:pk>', ProfileDetail.as_view(), name='view_profile_detail'),
    # path('update/<int:pk>', UpdateProfileDetail.as_view(), name='update profiles'),
   
   
]