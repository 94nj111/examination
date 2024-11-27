from django.contrib import admin
from django.urls import path, include

from todo.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
]

app_name = "todo"
