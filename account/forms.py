from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2',)

class NewProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #fields = ('username','email','password1','password2',)