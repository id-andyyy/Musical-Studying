from tasks.views import *
from django.urls import path


urlpatterns = [
    path("", tasks, name='tasks'),
    path("<int:id_>/theory/", task_theory, name='task_theory'),
    path("<int:id_>/exercises/", task_exercises, name='task_exercises'),
    path("<int:id_>/check/", task_check, name='task_check'),
]
