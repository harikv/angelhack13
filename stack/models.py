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

	company_name = models.CharField(max_length=200, blank = True, null = True, verbose_name='Company Name')
	company_description = models.CharField(max_length=1000, blank = True, null = True, verbose_name='Company Description')
	company_type_of_application = models.CharField(max_length=1000, blank = True, null = True, verbose_name='Type of application')

	frontend_languages = models.CharField(max_length=200, blank = True, null = True, verbose_name='Languages')
	frontend_framework = models.CharField(max_length=200, blank = True, null = True, verbose_name='Framework')
	frontend_libraries = models.CharField(max_length=200, blank = True, null = True, verbose_name='Libraries')
	frontend_description = models.CharField(max_length=1000, blank = True, null = True,verbose_name='Why did you use these?')

	backend_languages = models.CharField(max_length=200, blank = True, null = True, verbose_name='Languages')
	backend_framework = models.CharField(max_length=200, blank = True, null = True, verbose_name='Framework')
	backend_libraries = models.CharField(max_length=200, blank = True, null = True, verbose_name='Libraries')
	backend_description = models.CharField(max_length=1000, blank = True, null = True, verbose_name='Why did you use these?')

	database = models.CharField(max_length=200, blank = True, null = True, verbose_name='Databases')
	database_description = models.CharField(max_length=1000, blank = True, null = True, verbose_name='Why did you use these?')

	server_os = models.CharField(max_length=200, blank = True, null = True, verbose_name='OS')
	server_configuration = models.CharField(max_length=200, blank = True, null = True, verbose_name='Configuration')
	server_ram = models.CharField(max_length=200, blank = True, null = True, verbose_name='RAM')
	server_nodes = models.CharField(max_length=200, blank = True, null = True, verbose_name='#Nodes')
	server_hosting_provider = models.CharField(max_length=200, blank = True, null = True, verbose_name='Hosting Provider')
	server_description = models.CharField(max_length=1000, blank = True, null = True, verbose_name='Why did you use these?')
	#connection to kiran's model