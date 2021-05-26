# Django
from django.urls import path

# Views
from base import views
from django.contrib.auth.views import LogoutView

app_name = 'base'
urlpatterns = [
    path('login', views.CustomerLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='base:login'), name='logout'),
    path('register', views.RegisterPage.as_view(), name='register'),

    path('', views.TaskList.as_view(), name='feed'),
    path('create', views.TaskCreate.as_view(), name='create'),
    path('detail/<int:pk>', views.TaskDetail.as_view(), name='detail'),
    path('update/<int:pk>', views.TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.TaskDelete.as_view(), name='delete'),
]