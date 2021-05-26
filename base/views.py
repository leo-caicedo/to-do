# Django
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.views import LoginView    
from django.urls import reverse_lazy

# Models
from base.models import Task


class CustomerLoginView(LoginView):

    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base:feed')


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


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('base:feed')