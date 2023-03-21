from .views import *
from rest_framework import routers
from django.urls import path, include 
from knox import views as knox_views 
from .views import PasswordRecoveryView, PasswordResetView

urlpatterns = [
	path('register', SignUpAPI.as_view()),
	path('login', SignInAPI.as_view()),
	path('check_username',UsernameAPI.as_view()),
	path('send_otp',sendOtpViewSet.as_view()),
	path('check_otp',checkOtpViewSet.as_view()),
	path('verify_email/<str:token>/',verify_email.as_view()),
	path('password-recovery/', PasswordRecoveryView.as_view(), name='password_recovery'),
    path('password-reset/<int:user_id>/<str:token>/', PasswordResetView.as_view(), name='password_reset'),
	path('logout', knox_views.LogoutView.as_view(), name="knox-logout"),

] 