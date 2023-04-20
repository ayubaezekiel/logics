from .models import Profile
from django.urls import reverse
from .forms import RegisterForm,NewProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin 
from django.views.generic import TemplateView,CreateView,UpdateView


# Create your views here.

class LoginView(LoginView):
    template_name = 'login.html'

class UserRegistration(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url= '/login'


class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard.html'
    login_url = '/login'

class NewProfile(SuccessMessageMixin,UpdateView):
    template_name = 'new_profile.html'
    form_class = NewProfileForm
    model = Profile
    success_message = 'Profile updated successfully'
    success_url= '/dashboard'

        
    
   

