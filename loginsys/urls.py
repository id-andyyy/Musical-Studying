from loginsys.views import *
from django.urls import path


urlpatterns = [
    path("login/", user_login, name='login'),
    path("register/", user_register, name='register'),
    path("logout/", user_logout, name='logout'),
]