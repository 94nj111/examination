from django.urls import reverse_lazy
from django.views import generic

from todo.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").order_by("done")
    template_name = "todo/index.html"
    paginate_by = 4
    
    
class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")
    
    
class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")
    
    
class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")
