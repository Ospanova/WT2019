from django.urls import path
from api import views

urlpatterns = [
    path(r'contact/<int:pk>/', views.ContactDetail.as_view()),
    path(r'contact/', views.ContactView.as_view()),
    path(r'login/', views.login),
    path(r'logout/', views.logout),
]
