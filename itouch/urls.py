from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('view/<str:pk>/', views.viewPhoto, name='Photo'),
    path('add/', views.addPhoto, name='add'),
]