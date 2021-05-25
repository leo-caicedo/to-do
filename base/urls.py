# Django
from django.urls import path

# Views
from base import views

app_name = 'base'
urlpatterns = [
    path('', views.TaskList.as_view(), name='feed'),

]