# Django
from django.views.generic.list import ListView

# Models
from base.models import Task

class TaskList(ListView):
    
    model = Task
    context_object_name = 'tasks'