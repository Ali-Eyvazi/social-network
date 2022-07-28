from django.shortcuts import render,get_object_or_404,redirect
from django.views import View 
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Post
from django.contrib import messages
from .forms import PostUpdateForm
from django.utils.text import slugify



class PostView(LoginRequiredMixin,View):
    def get(self,request):
        posts=Post.objects.filter(user=request.user)
        return render (request,'posts/my_posts.html',{'posts':posts})



class PostDetailView(LoginRequiredMixin,View):
    def get(self,request,post_id,post_slug):

        post=get_object_or_404(Post,id=post_id,slug=post_slug)
        return render(request,'posts/details.html',{'post':post})


        

class PostDeleteView(LoginRequiredMixin,View):
    def get(self,request ,post_id):
        post=get_object_or_404(Post,id=post_id)
        if post.user.id== request.user.id:
            post.delete()
            messages.success(request,'post deleted successfuly','success')

        else:

            messages.error(request,'you cannot delete this post','danger')
        return redirect('home:home')

class PostUpdateView(View):
    
    form_class=PostUpdateForm


    def setup(self,request,*args,**kwargs):
        self.post_instance=Post.objects.get(id=kwargs['post_id'])
        return super().setup(request,*args,**kwargs)


    def dispatch(self, request,*args,**kwarg) :
        post=self.post_instance
        if not post.user.id ==request.user.id:
            messages.error(request,'you are not allow to remove this post ','danger')
            return redirect ('home:home')

        return super().dispatch(request,*args,**kwarg)

   

    def get(self,request,*args,**kwargs):

        post=self.post_instance
        form=self.form_class(instance=post)
        return render(request,'posts/update.html',{'form':form})



    def post(self,request,*args,**kwargs):
        post=self.post_instance
        form=self.form_class(request.POST,instance=post)
        if form.is_valid():

            new_post=form.save(commit=False)
            new_post.slug=slugify(form.cleaned_data['body'][:15])
            new_post.save()
            
            messages.success(request,'you have updated post successfully', 'success')
        return redirect('posts:details', post.id,post.slug)




class PostCreateView(LoginRequiredMixin,View):
    form_class=PostUpdateForm
    def get(self,request):
        form=self.form_class()
        return render(request,'posts/create.html',{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            create_post=form.save(commit=False)
            create_post.slug=slugify(form.cleaned_data['body'][:15])
            create_post.user=request.user
            create_post.save()
            messages.success(request,'you have created new post successfully','success')
            return redirect('posts:details',create_post.id,create_post.slug)
        








    
       