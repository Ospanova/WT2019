from django.urls import path 
from api import views
from api import auth
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('task_lists/', views.task_lists),
    path('task_lists/<int:pk>/', views.task_list_details),
    path('task_lists/<int:pk>/tasks/', views.task_list_tasks),
    path('tasks/<int:pk>/', views.task_details),
]
