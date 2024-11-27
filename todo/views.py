from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect

from todo.models import Tag, Task
from todo.forms import TaskForm


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").order_by("done")
    template_name = "todo/index.html"
    paginate_by = 4
    
    
class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")
    
    
class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")
    
    
class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")
    
    
class TaskToggleView(generic.View):
    @staticmethod
    def post(request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.done:
            task.done = False
        else:
            task.done = True
        task.save()
        return redirect("todo:index")
