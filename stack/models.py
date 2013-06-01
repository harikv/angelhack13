from django.db import models

# Create your models here.

class ComponentList(models.Model):
	component_name = models.CharField(max_length=64, null=True, default=None, blank=True)

class StackItem(models.Model):
	item_tag = models.CharField(max_length=64, null=True, default=None, blank=True)
	item_type = models.CharField(max_length=64, null=True, default=None, blank=True)
	item_component = models.ForeignKey(ComponentList, null=True, blank=True, default=None)
	item_justification = models.CharField(max_length=1024, null=True, default=None, blank=True)

class TechStack(models.Model):
	stack_item = models.ForeignKey(StackItem, null=True, default=None, blank=True, related_name='tech_stack')
	domain = models.CharField(max_length=128, null=True, default=None, blank=True)
	#connection to kiran's model