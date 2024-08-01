from django.urls import path
from . import views

urlpatterns = [
    path('/home', views.home, name='home'),
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<int:pk>/edit/', views.edit_blog, name='edit_blog'),
    path('<int:pk>/delete/', views.delete_blog, name='delete_blog'),
]
