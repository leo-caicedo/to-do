# Django
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin   
from django.urls import reverse_lazy

# Models
from base.models import Task


class CustomerLoginView(LoginView):

    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base:feed')


class TaskList(LoginRequiredMixin,ListView):
    
    model = Task
    context_object_name = 'tasks'


class TaskDetail(LoginRequiredMixin,DetailView):

    model = Task
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin,CreateView):

    model = Task
    fields = '__all__'
    success_url = reverse_lazy('base:feed')


class TaskUpdate(LoginRequiredMixin,UpdateView):

    model = Task
    fields = '__all__'
    success_url = reverse_lazy('base:feed')


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('base:feed')