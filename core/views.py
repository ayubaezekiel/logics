from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name ='index.html'
    
class NewsView(TemplateView):
    template_name = 'news.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

