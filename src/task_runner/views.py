from django.views.generic import FormView

from .forms import TaskModelForm


class NewTaskFormView(FormView):
    form_class = TaskModelForm
    template_name = "task_runner/new_task.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
