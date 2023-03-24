from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    #path('logout/', views.logout, name='logout'),
    path('create-room/', views.createRoom, name='create-room'),
]