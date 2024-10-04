from songs.views import *
from django.urls import path


urlpatterns = [
    path("", songs, name='songs'),
]