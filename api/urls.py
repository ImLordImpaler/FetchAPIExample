from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.apiOverview , name='api-Overview'),
    path('task-list/' , views.taskList , name = 'tasks' ),
    path('task/<str:pk>/' , views.taskDesc , name = 'taskDesc'),
    path('newTask/' , views.createTask , name = 'createTask'),
    path('updateTask/<str:pk>/' , views.updateTask , name = 'updateTask'),
    path('deleteTask/<str:pk>/' , views.deleteTask , name = 'deleteTask'),
]
