from django.urls import path
from django.views import View

from catalog.views import (
    TagListView,
    TagCreateView,
    TagUpdateView,
    TaskCreateView,
    TaskUpdateView,
    TaskListView,
    TagDeleteView,
    TaskDeleteView,
    TaskToggleCompleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("tag/create/", TagCreateView.as_view(), name="tags-create"),
    path("tag/update/<int:pk>/", TagUpdateView.as_view(), name="tags-update"),
    path("tag/delete/<int:pk>/", TagDeleteView.as_view(), name="tags-delete"),
    path("task/<int:pk>/toggle/", TaskToggleCompleteView.as_view(), name="task-toggle"),
]

app_name = "catalog"
