from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiUrl, name='api-url'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<id>/', views.taskDetail, name='task-detail'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<id>/', views.taskUpdate, name='task-update'),
    path('task-delete/<id>/', views.taskDelete, name='task-delete')
]