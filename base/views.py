# Django
from django.views.generic import ListView, DetailView

# Models
from base.models import Task

class TaskList(ListView):
    
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):

    model = Task
    context_object_name = 'task'