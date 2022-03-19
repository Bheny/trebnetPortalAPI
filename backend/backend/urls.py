
from django.contrib import admin
from django.urls import path,include 
from rest_framework import routers  
from api.views import *
#from rest_framework.generics import ListCreateAPIView

router = routers.DefaultRouter()
router.register('projects', ProjectView, 'project')
router.register('profiles', ProfileView, 'profile')
router.register('users', UserView, 'user')
router.register('transaction', TransactionView, 'transaction')
router.register('event', EventView, 'event')
router.register('teams', TeamView, 'team')
router.register('jobs', JobView, 'job')
router.register('questions', QuestionView, 'question')
router.register('idea', IdeaView, 'idea')
router.register('news', NewsView, 'news')
router.register('announcement', AnnouncementView, 'announcement')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('transactions/', ListCreateAPIView.as_view(), name='Transactions'),
    path('auth/', include('Auth.urls')),
    path('send_credits/', send_credits)
]
