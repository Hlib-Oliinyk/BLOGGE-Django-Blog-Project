from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name = 'posts'),
    path('post/<int:post_id>', views.post_details, name = 'post'),
    path('post/<int:post_id>/update/', views.PostsUpdateView.as_view(), name = 'update'),
    path('create', views.create, name = "create"),
    path('about', views.about, name = "about"),
    path('contact', views.contact, name = "contact"),
]