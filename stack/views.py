# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView

class LandingPageView(TemplateView):
    template_name = "landing.html"

class CompanyPageView(TemplateView):
    template_name = "company.html"
