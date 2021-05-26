# Django
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from django.contrib.auth.views import LoginView, redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin   
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect

# Forms
from django.contrib.auth.forms import UserCreationForm

# Models
from base.models import Task


class CustomerLoginView(LoginView):

    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base:feed')


class RegisterPage(FormView):

    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('base:feed')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('base:feed')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin,ListView):
    
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin,DetailView):

    model = Task
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin,CreateView):

    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('base:feed')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin,UpdateView):

    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('base:feed')


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('base:feed')