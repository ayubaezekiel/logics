from django.urls import path
from .views import AboutView,ContactView,HomeView,NewsView


app_name = 'core'

urlpatterns = [
    path('',HomeView.as_view() ,name='home'),
    path('news/',NewsView.as_view() ,name='news'),
    path('about/',AboutView.as_view() ,name='about'),
    path('contact/',ContactView.as_view() ,name='contact'),
]