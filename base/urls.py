# Django
from django.urls import path

# Views
from base import views

app_name = 'base'
urlpatterns = [
    path('', views.TaskList.as_view(), name='feed'),
    path('create', views.TaskCreate.as_view(), name='create'),
    path('detail/<int:pk>', views.TaskDetail.as_view(), name='detail'),
    path('update/<int:pk>', views.TaskUpdate.as_view(), name='update'),
]