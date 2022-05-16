from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

app_name = 'auth'

urlpatterns = [
	path('register/', csrf_exempt(register), name="register"),
	#path('register/', register, name="register"),
	path('login/', login, name="login"),
	path('logout/', logout, name="logout"),
]