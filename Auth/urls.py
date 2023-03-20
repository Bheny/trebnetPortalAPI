from django.urls import path, include
from .views import *
from .views import ChangePasswordView
# from django.views.decorators.csrf import csrf_exempt
from knox import views as knox_views
app_name = 'auth'

urlpatterns = [
	path('',include('knox.urls')),
	path('register', SignUpAPI.as_view()),
	path('login', SignInAPI.as_view()),
	path('change-password/', ChangePasswordView.as_view(), name='change-password'),
	path('logout', knox_views.LogoutView.as_view(), name="knox-logout"),

]