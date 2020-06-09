from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logOut, name='logout'),
    
    path('', views.home, name='home'),
    path('create_client/<str:pk>/', views.addClient, name='create_client'),
    path('delete_client/<str:pk>/', views.deleteClient, name='delete_client')
]
