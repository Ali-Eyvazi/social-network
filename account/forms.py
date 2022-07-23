from logging import PlaceHolder
from django import forms





class UserRegistrationForm(forms.Form):
    
    name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Enter your username','class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your Email address','class':'form-control'}))
    password=forms.CharField(max_length=35,widget=forms.PasswordInput(attrs={'placeholder':'Enter your password','class':'form-control'}))
    phone_number=forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Enter your phone number','class':'form-control'})) 