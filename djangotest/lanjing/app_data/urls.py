from django.urls import path
from app_data import views
urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('update/', views.update),
    path('delete/', views.delete),
    path('search/', views.search),
]