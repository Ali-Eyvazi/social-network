from genericpath import exists
from operator import is_
from sre_constants import SUCCESS
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpRequest
from .forms import EdirUserForm, UserRegistrationForm,UserLoginForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Relation


class UserRegisterView(View):

    def dispatch(self, request: HttpRequest, *args: any, **kwargs: any) :
        
        if request.user.is_authenticated:
            return redirect('home:home')
        
        return super().dispatch(request, *args, **kwargs)

    form_class=UserRegistrationForm
    template_name='account/register.html'
    
    def get(self,request):
        form=self.form_class()
        return render (request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create_user(cd["username"],cd['email'],cd['password2'])
            
            messages.success(request,'you have rgistered succesfully', 'success')
            return redirect ('home:home')
        
        return render (request,self.template_name,{'form':form})   

        
        

        
        
        
class UserLoginView(View):
    form_class=UserLoginForm
    template_name='account/login.html'


    def setup(self, request: HttpRequest, *args: any, **kwargs: any) -> None:

        self.next=request.GET.get('next')

        return super().setup(request, *args, **kwargs)




    def dispatch(self, request: HttpRequest, *args: any, **kwargs: any) :
        
        if request.user.is_authenticated:
            return redirect('home:home')
        
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})


    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,' you logged in successfully','success')
                if self.next:
                    return redirect(self.next)
                return redirect('home:home')
            else:
                messages.error(request,'The username or password is wrong','warning')


        return render(request,self.template_name,{'form':form})





class UserLogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,'you have successfully loged out','success')

        return redirect('home:home')




class UserProfileView(LoginRequiredMixin,View):


    def get(self,request,user_id):
        is_following=False
        user=User.objects.get(pk=user_id)
        posts=user.posts.all()

        relation=Relation.objects.filter(from_user=request.user  ,to_user=user)
        if relation.exists():
            is_following=True
        return render (request,'account/profile.html',{'user':user , 'posts': posts,'is_following':is_following})


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name='account/password_reset_form.html'
    success_url=reverse_lazy('account:password_reset_done')
    email_template_name='account/password_reset_email.html'



class UserPAsswordResetDonView(auth_views.PasswordResetDoneView):
    template_name='account/password_reset_done.html'

    

class UserPasswordresetConfirmView(auth_views.PasswordResetConfirmView):
    template_name='account/password_reset_confirm.html'
    success_url=reverse_lazy('account:password_reset_complete')


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name='account/password_reset_complet.html'

class UserFollowView(LoginRequiredMixin,View):
    def get(self,request,user_id):
        user=User.objects.get(id=user_id)
        relation=Relation.objects.filter(from_user=request.user,to_user=user)
        if relation.exists():
            messages.error(request,'you are already following this user', 'danger')


        else:
            Relation(from_user=request.user,to_user=user).save()
            messages.success(request,'you followed this user','success')

        return redirect('account:user_profile',user.id)

class UserUnfollowView(LoginRequiredMixin,View):
    def get(self,request,user_id):
        user=User.objects.get(id=user_id)
        relation=Relation.objects.filter(from_user=request.user,to_user=user)
        if relation.exists():
            relation.delete()
            messages.success(request,' you are unfollowed this user','success')


        else:
            messages.error(request,'you are not following this user ','warning')

        return redirect('account:user_profile',user.id)






class EditUserView(LoginRequiredMixin,View):
    form_class=EdirUserForm
    
    
    def get(self,request):
        form=self.form_class(instance=request.user.userdetails,initial={'email':request.user.email})
        return render(request,'account/Edit_profile.html',{'form':form})
        
    def post(self,request):
        form=self.form_class(request.POST,instance=request.user.userdetails)
        if form.is_valid():
            form.save()
            request.user.email=form.cleaned_data['email']
            request.user.save()

            messages.success(request,'profile edited successfully','success')


        return redirect ('account:user_profile',request.user.id)







