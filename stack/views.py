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
	
	def get_context_data(self, **kwargs):
		context = super(LandingPageView, self).get_context_data(**kwargs)
		context['featured_list']=TechStack.get_featured_list()
 		return context

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


class SearchListView(ListView):
	model=TechStack
	context_object_name = 'object_list'
	template_name = 'search_results.html'

	def get_queryset(self):
		queryset=[]
		try:
			from itertools import chain
			tag = self.request.GET['q']
			q1 = TechStack.objects.filter(frontend_languages__icontains=tag).order_by('-id')
			q2 = TechStack.objects.filter(company_name__icontains=tag).order_by('-id')
			q3 = TechStack.objects.filter(frontend_framework__icontains=tag).order_by('-id')
			q4 = TechStack.objects.filter(frontend_libraries__icontains=tag).order_by('-id')
			q5 = TechStack.objects.filter(backend_languages__icontains=tag).order_by('-id')
			q6 = TechStack.objects.filter(backend_framework__icontains=tag).order_by('-id')
			q7 = TechStack.objects.filter(database__icontains=tag).order_by('-id')
			q8 = TechStack.objects.filter(server_os__icontains=tag).order_by('-id')
			q9 = TechStack.objects.filter(server_hosting_provider__icontains=tag).order_by('-id')
			queryset=chain(q1,q2,q3,q4,q5,q6,q7,q8,q9)
		except:
			pass
		return queryset

	def get_context_data(self, **kwargs):
		context = super(SearchListView, self).get_context_data(**kwargs)
		try:
			context['search_term'] = self.request.GET['q']
		except:
			context['search_term'] = 'nothing'
 		return context