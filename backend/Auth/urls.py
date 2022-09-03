from django.urls import path, include
from .views import *
# from django.views.decorators.csrf import csrf_exempt
from knox import views as knox_views
app_name = 'auth'

urlpatterns = [
	path('',include('knox.urls')),
	path('register', SignUpAPI.as_view()),
	path('login', SignInAPI.as_view()),
	path('logout', knox_views.LogoutView.as_view(), name="knox-logout"),

]