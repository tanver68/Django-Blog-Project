from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

#Create Registation form

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]
        
#Create User Update form
        
class UserUpdateForm(forms.ModelForm):
     email = forms.EmailField()
    
     class Meta:
         model = User
         fields = ['username', 'email']

#Create Profile update form

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = profile
        fields = ['image']
    
    