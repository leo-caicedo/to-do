# Django
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
    
from django.urls import reverse_lazy

# Models
from base.models import Task

class TaskList(ListView):
    
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):

    model = Task
    context_object_name = 'task'


class TaskCreate(CreateView):

    model = Task
    fields = '__all__'
    success_url = reverse_lazy('base:feed')


class TaskUpdate(UpdateView):

    model = Task
    fields = '__all__'
    success_url = reverse_lazy('base:feed')