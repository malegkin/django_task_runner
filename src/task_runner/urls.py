from django.urls import path

from .views import NewTaskFormView

app_name = "task_runner"

urlpatterns = [
    path("", NewTaskFormView.as_view(), name="new_task"),
]
