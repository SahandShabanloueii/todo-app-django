from django.urls import path
from task.views import (
    show_task
)

urlpatterns = [
    path('', show_task, name='show_task')
]
