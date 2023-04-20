from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import DashboardView,UserRegistration,NewProfile,LoginView


app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('register/',UserRegistration.as_view() ,name='register'),
    path('dashboard/',DashboardView.as_view() ,name='dashboard'),
    path('update_profile/<pk>',NewProfile.as_view() ,name='update_profile'),
]