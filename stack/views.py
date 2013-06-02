# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.forms.models import inlineformset_factory
from stack.models import StackItem, TechStack, ComponentList
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from stack.forms import TechStackForm
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect

from django.template import RequestContext
from django.views.generic import ListView, DetailView, TemplateView

class LandingPageView(TemplateView):
	template_name = "landing.html"
	
	def get_context_data(self, **kwargs):
		context = super(LandingPageView, self).get_context_data(**kwargs)
		context['featured_list']=TechStack.get_featured_list()
 		return context

class CompanyPageView(DetailView):
    template_name = "company.html"
    model = TechStack
    context_object_name = 'stack'

    def get_object(self):
        # Call the superclass
        company_slug = self.kwargs['company_slug']
        object = get_object_or_404(TechStack, company_slug=company_slug)
        #object = TechStack.objects.get(id=1)

        return object

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CompanyPageView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['company_name'] = self.object.company_name
        context['company_description'] = self.object.company_description
        context['company_type_of_application'] = self.object.company_type_of_application.split()

        context['frontend_languages'] = self.object.frontend_languages.split()
        context['frontend_framework'] = self.object.frontend_framework.split()
        context['frontend_libraries'] = self.object.frontend_libraries.split()
        context['frontend_description'] = self.object.frontend_description

        context['backend_languages'] = self.object.frontend_libraries.split()
        context['backend_framework'] = self.object.backend_framework.split()
        context['backend_libraries'] = self.object.backend_libraries.split()
        context['backend_description'] = self.object.backend_description

        context['database'] = self.object.database.split()
        context['database_description'] = self.object.database_description

        context['server_os'] = self.object.server_os
        context['server_configuration'] = self.object.server_configuration
        context['server_ram'] = self.object.server_ram
        context['server_nodes'] = self.object.server_nodes
        context['server_hosting_provider'] = self.object.server_hosting_provider
        context['server_description'] = self.object.server_description

        return context


def CreateStackForm(request):
    if request.method == 'POST':
        form = TechStackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('company_page', args=[form.instance.company_slug]))
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
