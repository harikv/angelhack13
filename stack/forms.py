from django.forms.models import inlineformset_factory
from stack.models import StackItem, TechStack, ComponentList
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django import forms
'''
def FrontendFormsetHelper(domain=None):
	if domain is not None:
		StackItemFormset =  inlineformset_factory(ComponentList, StackItem, max_num=3, extra=3)
		try:
			req_stack = TechStack.objects.get(domain=domain)
			req_component = ComponentList.objects.get(component_name="Frontend")
			formset = StackItemFormset(instance=req_component, queryset = StackItem.objects.filter(tech_stack = req_stack))
			return formset
		except ObjectDoesNotExist:
			req_component = ComponentList.objects.get(component_name="Frontend")
			formset = StackItemFormset(queryset = StackItem.objects.none(), initial=[
				{'item_type':'Language', },
				{'item_type':'Framework', },
				{'item_type':'Library', }
				])
			return formset

def BackendFormsetHelper(domain=None):
	if domain is not None:
		StackItemFormset =  inlineformset_factory(ComponentList, StackItem, max_num=3, extra=3)
		try:
			req_stack = TechStack.objects.get(domain=domain)
			req_component = ComponentList.objects.get(component_name="Backend")
			formset = StackItemFormset(instance=req_component, queryset = StackItem.objects.filter(tech_stack = req_stack))
			return formset
		except ObjectDoesNotExist:
			req_component = ComponentList.objects.get(component_name="Backend")
			formset = StackItemFormset(queryset = StackItem.objects.none(), initial=[
				{'item_type':'Language', },
				{'item_type':'Framework', },
				{'item_type':'Library', }
				])
			return formset

def ServerFormsetHelper(domain=None):
	if domain is not None:
		StackItemFormset =  inlineformset_factory(ComponentList, StackItem, max_num=3, extra=3)
		try:
			req_stack = TechStack.objects.get(domain=domain)
			req_component = ComponentList.objects.get(component_name="Server")
			formset = StackItemFormset(instance=req_component, queryset = StackItem.objects.filter(tech_stack = req_stack))
			return formset
		except ObjectDoesNotExist:
			req_component = ComponentList.objects.get(component_name="Server")
			formset = StackItemFormset(queryset = StackItem.objects.none(), initial=[
				{'item_type':'OS', },
				{'item_type':'Configuration', },
				{'item_type':'Hosting', }
				])
			return formset

def DatabaseFormsetHelper(domain=None):
	if domain is not None:
		StackItemFormset =  inlineformset_factory(ComponentList, StackItem, max_num=3, extra=3)
		try:
			req_stack = TechStack.objects.get(domain=domain)
			req_component = ComponentList.objects.get(component_name="Database")
			formset = StackItemFormset(instance=req_component, queryset = StackItem.objects.filter(tech_stack = req_stack))
			return formset
		except ObjectDoesNotExist:
			req_component = ComponentList.objects.get(component_name="Database")
			formset = StackItemFormset(queryset = StackItem.objects.none())
			return formset
'''

class TechStackForm(forms.ModelForm):    
    class Meta:
        model = TechStack
        exclude = ('domain', 'stack_item', 'company_slug' )
