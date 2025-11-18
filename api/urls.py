from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.getData),
    path('posts/add/', views.addPost),
    path('posts/<int:post_id>/', views.update_and_delete),
]