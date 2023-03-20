from django.urls import path
from .views import MissionList, MissionDetail, MissionApplicationList, MissionApplicationDetail

urlpatterns = [
    path('', MissionList.as_view(), name='viewmissions'),
    path('detail/<int:pk>', MissionDetail.as_view(), name='view_missions_detail'),
     path('applications', MissionApplicationList.as_view(), name='view_missionsApplications'),
    path('application/detail/<int:pk>', MissionApplicationDetail.as_view(), name='view_missionsApplication_detail'),
    # path('update/<int:pk>', UpdateProfileDetail.as_view(), name='update profiles'),
    # path('driver/apply/',Driver_Application.as_view(), name='apply'),
   
]
