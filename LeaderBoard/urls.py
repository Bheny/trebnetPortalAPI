from django.urls import path
from .views import TransactionList, TransactionDetail

urlpatterns = [
    path('', TransactionList.as_view(), name='view_Transactions'),
    path('detail/<int:pk>', TransactionDetail.as_view(), name='view_profiles'),
    # path('update/<int:pk>', UpdateProfileDetail.as_view(), name='update profiles'),
    # path('driver/apply/',Driver_Application.as_view(), name='apply'),
   
]
