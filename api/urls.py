from django.urls import path

from api.views import (
    todo_list,
    todo_detail,
    category_list,
    category_detail
)

urlpatterns = [
    path('tasks/', todo_list, name="todo_list"),
    path('tasks/<int:id>/', todo_detail, name="todo_detail"),
    path('categories/', category_list, name="category_list"),
    path('categories/<int:id>/', category_detail, name="category_detail"),
]