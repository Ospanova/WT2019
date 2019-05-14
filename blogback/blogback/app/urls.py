from django.urls import path
from app import fbs
from app import auth
urlpatterns = [
    path('users/', auth.UserList.as_view()),
    path('login/', auth.login),
    path('logout/', auth.logout),
    path('post/', fbs.post_list),
    path('post/<int:pk>/', fbs.post_details),
]
