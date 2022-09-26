
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import *
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
#from rest_framework.generics import ListCreateAPIView

router = routers.DefaultRouter()
router.register('projects', ProjectView, 'project')
router.register('profiles', ProfileView, 'profiles')
router.register('profile/detail', ProfileDetailView, 'profile_detail')
router.register('users', UserView, 'user')
router.register('transaction', TransactionView, 'transaction')
router.register('event', EventView, 'event')
router.register('teams', TeamView, 'team')
router.register('jobs', JobView, 'job')
router.register('questions', QuestionView, 'question')
router.register('idea', IdeaView, 'idea')
router.register('news', NewsView, 'news')
router.register('announcement', AnnouncementView, 'announcement')
router.register('rank', RankView, 'rank')
router.register('client', ClientView, 'client')
router.register('service', ServiceView, 'service')
router.register('serviceRequests', ServiceRequestView, 'serviceRequest')
router.register('serviceRequest/detail', ServiceRequestDetailView, 'service_request_detail')
router.register('JobRequest', JobRequestView, 'JobRequest')
router.register('Notes', NoteView, 'Notes')





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('transactions/', ListCreateAPIView.as_view(), name='Transactions'),
    path('auth/', include('Auth.urls')),
    path('send_credits/', send_credits),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
