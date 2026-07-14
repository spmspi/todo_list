from django.shortcuts import render, redirect
from catalog import models
from catalog.models import Task
from django.views import generic, View
from django.views.generic import DetailView, CreateView, UpdateView, ListView



def index(request):
    num_tasks = models.Task.objects.all().count()
    active_tasks = models.Task.objects.filter(is_completed=False).count()
    complete_tasks = models.Task.objects.filter(is_completed=True).count()
    context = {
        "num_tasks": num_tasks,
        "active_tasks": active_tasks,
        "complete_tasks": complete_tasks,
    }
    return render(request, "catalog/index.html", context=context)


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "catalog/task_list.html"

