
from django.contrib import admin
from django.urls import path,  include , re_path
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#from rest_framework.generics import ListCreateAPIView

# router = routers.DefaultRouter()
# router.register('projects', ProjectView, 'project')
# router.register('profiles', ProfileView, 'profiles')
# router.register('profile/detail', ProfileDetailView, 'profile_detail')
# router.register('users', UserView, 'user')
# router.register('transaction', TransactionView, 'transaction')
# router.register('event', EventView, 'event')
# router.register('teams', TeamView, 'team')
# router.register('jobs', JobView, 'job')
# router.register('questions', QuestionView, 'question')
# router.register('idea', IdeaView, 'idea')
# router.register('news', NewsView, 'news')
# router.register('announcement', AnnouncementView, 'announcement')
# router.register('rank', RankView, 'rank')
# router.register('client', ClientView, 'client')
# router.register('service', ServiceView, 'service')
# router.register('serviceRequests', ServiceRequestView, 'serviceRequest')
# router.register('serviceRequest/detail', ServiceRequestDetailView, 'service_request_detail')
# router.register('JobRequest', JobRequestView, 'JobRequest')
# router.register('Notes', NoteView, 'Notes')



schema_view = get_schema_view(
   openapi.Info(
      title="TREBNET PORTAL API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('admin/', admin.site.urls),
    path('auth/', include('Authentication.urls')),
    path('profile/', include('Profiles.urls')),
    path('rank/', include('Ranks.urls')),
    path('class/', include('Class.urls')),
    path('mission/', include('Missions.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
   
   #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name="index.html"))]



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('media/', serve,{'document_root': settings.MEDIA_ROOT}),
#     path('static/', serve,{'document_root': settings.STATIC_ROOT}),
# ]
