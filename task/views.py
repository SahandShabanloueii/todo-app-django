from django.shortcuts import render
from django.http import HttpResponseRedirect
from task.models import TodoTask, Category
from task.forms import TaskCreatForms

def show_task(request):
    query = TodoTask.objects.all().order_by('created')

    form = TaskCreatForms(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = TaskCreatForms()

    dic = {
        'query' : query,
        'form' : form,
    }

    return render(request, 'task/index.html', dic)
