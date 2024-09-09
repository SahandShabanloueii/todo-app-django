from django.urls import path
from task.views import (
    show_task,
    TaskDetail,
    delete_task
)

urlpatterns = [
    path('', show_task, name="show_task"),
    path('task/<int:pk>', TaskDetail.as_view(), name="task_detail"),
    path('<int:id>/delete', delete_task, name="delete_task"),
]