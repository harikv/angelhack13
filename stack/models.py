from django.db import models

# Create your models here.

class TechStack(models.model):
	stack_item = models.ForeignKey(StackItem, null=True, default=None, blank=True)
	#connection to kiran's model

class StackItem(models.model):
	item_tag = models.CharField(max_length=64, null=True, default=None, blank=True)
	item_type = models.CharField(max_length=64, null=True, default=None, blank=True)
	item_component = models.CharField(max_length=64, null=True, default=None, blank=True)
	item_justification = models.CharField(max_length=1024, null=True, default=None, blank=True)