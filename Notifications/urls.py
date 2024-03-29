from django.urls import path
from .views import *

urlpatterns = [
    path('', NotificationList.as_view(), name='viewnotification'),
    path('detail/<int:pk>', NotificationDetail.as_view(), name='view_notification_detail'),
    path('notifications/<int:id>', NotificationList.as_view(),name="subscribe"),
    path('testing/', index, name="test_page")
]
