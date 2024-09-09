from django import forms
from task.models import TodoTask

class DataInput(forms.DateInput):
    input_type = 'date'

class TaskCreateForm(forms.ModelForm):
    created = forms.DateField(widget=DataInput)
    class Meta:
        model = TodoTask
        fields = ('title', 'content', 'created', 'category')
