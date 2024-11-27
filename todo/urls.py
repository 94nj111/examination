from django.contrib import admin
from django.urls import path, include

from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskCreateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
]

app_name = "todo"
