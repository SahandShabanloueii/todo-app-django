from rest_framework import serializers
from todo.models import TodoTask

class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = ['title', 'content', 'created', 'category']