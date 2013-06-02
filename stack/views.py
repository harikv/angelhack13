# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.forms.models import inlineformset_factory
from stack.models import StackItem, TechStack, ComponentList
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from stack.forms import TechStackForm
from django.template import RequestContext

class LandingPageView(TemplateView):
    template_name = "landing.html"

class CompanyPageView(TemplateView):
    template_name = "company.html"



def CreateStackForm(request):
    if request.method == 'POST':
        form = TechStackForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = TechStackForm() # An unbound form

    return render_to_response('create-stack.html',{'form': form,} ,context_instance=RequestContext(request))


