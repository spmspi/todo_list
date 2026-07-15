from django.db.models import Model
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from catalog import models
from catalog.forms import TaskForm
from catalog.models import Task, Tag
from django.views import generic, View


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "catalog/index.html"

    def get_queryset(self):
        return Task.objects.all().order_by("-is_completed", "deadline")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task_list_form.html"
    success_url = reverse_lazy("catalog:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:index")
    template_name = "catalog/task_list_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:index")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "catalog/tags_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = [
        "name",
    ]
    template_name = "catalog/tags_list_form.html"
    success_url = reverse_lazy("catalog:tags-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = [
        "name",
    ]
    success_url = reverse_lazy("catalog:tags-list")
    template_name = "catalog/tags_list_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("catalog:tags-list")


class TaskToggleCompleteView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        return redirect("catalog:index")
