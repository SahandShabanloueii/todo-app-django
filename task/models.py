from django.db import models
from django import utils


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TodoTask(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created = models.DateField(default=utils.timezone.now())
    category = models.ForeignKey(Category, default='General', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
