from main.views import *
from django.urls import path


urlpatterns = [
    path("", main, name='main'),
]
