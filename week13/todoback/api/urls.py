from django.urls import path
from api.views import fbv, cbv, auth

urlpatterns = [
    path('task_lists/', fbv.task_lists),
    path('task_lists/<int:pk>/', fbv.task_list_details),
    path('task_lists/<int:pk>/tasks/', cbv.TaskListTasks.as_view()),
    path('tasks/<int:pk>/', cbv.TaskDetails.as_view()),
    path('users/', auth.Users.as_view()),
    path('login/', auth.login),
    path('logout/', auth.logout)
]