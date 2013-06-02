# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.forms.models import inlineformset_factory
from stack.models import StackItem, TechStack, ComponentList
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from stack.forms import TechStackForm
from django.template import RequestContext
import json
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

def GetTags(request):
	term = request.GET.get('term')
	parent = request.GET.get('parent')
	tag_list = TechStack.objects.values(parent).distinct()
	tag_match = list()
	for tags in tag_list:
		indiv_tags = str(tags.get(parent)).split(' ')
		for tag in indiv_tags:
			if term in tag.lower():
				tag_match.append(tag)
	return HttpResponse(json.dumps(tag_match), mimetype = "application/json")

