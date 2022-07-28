from django.shortcuts import render,get_object_or_404
from django.views import View 
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Post





class PostView(LoginRequiredMixin,View):
    def get(self,request):
        posts=Post.objects.filter(user=request.user)
        return render (request,'posts/my_posts.html',{'posts':posts})



class PostDetailView(LoginRequiredMixin,View):
    def get(self,request,post_id,post_slug):

        post=get_object_or_404(Post,id=post_id,slug=post_slug)
        return render(request,'posts/details.html',{'post':post})