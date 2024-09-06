from django.contrib import admin
from task.models import Category, TodoTask


admin.site.register(Category)
admin.site.register(TodoTask)

