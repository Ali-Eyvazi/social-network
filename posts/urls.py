from django import views
from django.contrib import admin
from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
        path('posts/',views.PostView.as_view(),name='posts'),
        path('details/<int:post_id>/<slug:post_slug>/',views.PostDetailView.as_view(),name='details'),
        path('post/delete/<int:post_id>',views.PostDeleteView.as_view(),name='delete'),
        path('post/update/<int:post_id>',views.PostUpdateView.as_view(),name='update'),
        path('post/create/',views.PostCreateView.as_view(),name='create'),


]