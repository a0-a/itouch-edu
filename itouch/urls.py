from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('view/<str:pk>/', views.viewPhoto, name='Photo'),
    path('add/', views.addPhoto, name='add'),
    path('user_gallery', views.user_gallery, name='user_gallery'),
]