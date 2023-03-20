from django.urls import path
from .views import RankList, RankDetail

urlpatterns = [
    path('', RankList.as_view(), name='view_ranks'),
    path('detail/<int:pk>', RankDetail.as_view(), name='view_profiles'),
    # path('update/<int:pk>', UpdateProfileDetail.as_view(), name='update profiles'),
    # path('driver/apply/',Driver_Application.as_view(), name='apply'),
   
]
