# Create your views here.
from django.forms.models import inlineformset_factory
from stack.models import StackItem, TechStack, ComponentList
from django.shortcuts import render_to_response
from stack.forms import FrontendFormsetHelper, BackendFormsetHelper, ServerFormsetHelper, DatabaseFormsetHelper
from django.http import HttpResponse
from django.core.context_processors import csrf

# def index(request):
# 	feformset = FrontendFormsetHelper("facebook.com")
# 	beformset = BackendFormsetHelper("facebook.com")
# 	seformset = ServerFormsetHelper("facebook.com")
# 	dbformset = DatabaseFormsetHelper("facebook.com")
# 	context = {"feformset": feformset, "beformset": beformset, "seformset": seformset, "dbformset": dbformset}
# 	context.update(csrf(request))
# 	return render_to_response("index.html", context)

# def submit(request, component=None):
# 	req_component = ComponentList.objects.get(pk=component)
# 	FrontendFormset = inlineformset_factory(ComponentList, StackItem)
# 	formset = FrontendFormset(request.POST, request.FILES, instance=req_component)
# 	if formset.is_valid():
# 		formset.save()
# 		return HttpResponse(status=200)
# 	else:
# 		return HttpResponse(status=500)