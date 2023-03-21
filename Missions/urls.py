from django.urls import path
from .views import *

urlpatterns = [
    path('', MissionList.as_view(), name='viewmissions'),
    path('filter',MissionFilter.as_view(), name="Filter Mission"),
    path('search',MissionSearch.as_view(), name="search Mission"),
    path('detail/<int:pk>', MissionDetail.as_view(), name='view_missions_detail'),
    path('applications', MissionApplicationList.as_view(), name='view_missionsApplications'),
    path('application/detail/<int:pk>', MissionApplicationDetail.as_view(), name='view_missionsApplication_detail'),
    # path('update/<int:pk>', UpdateProfileDetail.as_view(), name='update profiles'),
    # path('driver/apply/',Driver_Application.as_view(), name='apply'),
   
]
