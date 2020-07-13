"""Defines patterns for blogs URLs."""

from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # New Blog Post
    path('new_post/', views.new_post, name='new_post'),
    # Edit Blog Post
    path('edit_post/<int:entry_id>/', views.edit_post, name='edit_post'),
]
