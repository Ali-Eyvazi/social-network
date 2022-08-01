from logging import PlaceHolder
from django import forms
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError
from .models import UserDetails


class UserRegistrationForm(forms.Form):
    
    username=forms.CharField(min_length=6   ,max_length=30,widget=forms.TextInput(attrs={'placeholder':'Enter your username','class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your Email address','class':'form-control'}))
    password1=forms.CharField(label='password',max_length=35,widget=forms.PasswordInput(attrs={'placeholder':'Enter your password','class':'form-control'}))
    password2=forms.CharField(label='confirm password',max_length=35,widget=forms.PasswordInput(attrs={'placeholder':'Enter your password','class':'form-control'}))
    

    def clean_email(self) :
        email=self.cleaned_data['email']
        user=User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This email already exists')
         
        return email
        
    def clean_username(self):
        username=self.cleaned_data['username']
        user=User.objects.filter(username=username).exists()
        if user:
            raise ValidationError ('This username already exists')

        return username



    def clean(self) :
        cd=super().clean()
        pass1=cd.get('password1')
        pass2=cd.get('password2')

        if pass1 and pass2 and pass1!=pass2:
            raise ValidationError ('passwords must match')

        

class UserLoginForm(forms.Form):
    username=forms.CharField(label='username or email addres', max_length=30 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
class EdirUserForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=UserDetails
        fields=('age','bio',)    
   


   

    