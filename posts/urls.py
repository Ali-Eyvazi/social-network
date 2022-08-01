from django import views
from django.contrib import admin
from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
        path('posts/',views.PostView.as_view(),name='posts'),
        path('details/<int:post_id>/<slug:post_slug>/',views.PostDetailView.as_view(),name='details'),
        path('delete/<int:post_id>',views.PostDeleteView.as_view(),name='delete'),
        path('update/<int:post_id>',views.PostUpdateView.as_view(),name='update'),
        path('create/',views.PostCreateView.as_view(),name='create'),
        path('reply/<int:post_id>/<int:comment_id>',views.PostAddReplyView.as_view(),name='add_reply'),
        path('like/<int:post_id>/',views.PostLikeView.as_view(),name='post_like'),

]