from django.forms import ModelForm
from task.models import TodoTask

class TaskCreatForms(ModelForm):
    class Meta:
        model = TodoTask
        fields = ('title', 'created', 'category')

