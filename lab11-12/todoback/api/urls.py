from django.urls import path 
from api import views
urlpatterns = [
    path('task_lists/', views.task_lists),
    path('task_lists/<int:pk>/', views.task_list_details),
    path('task_lists/<int:pk>/tasks/', views.task_list_tasks),
    path('tasks/<int:pk>/', views.task_details),
]
