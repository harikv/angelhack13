from django.db import models
from django.db.models.signals import post_init, pre_init, post_save, pre_save
from django.template.defaultfilters import slugify
from django.dispatch import receiver

# Create your models here.

class ComponentList(models.Model):
	component_name = models.CharField(max_length=64, null=True, default=None, blank=True)

class StackItem(models.Model):
	item_tag = models.CharField(max_length=64, null=True, default=None, blank=True)
	item_type = models.CharField(max_length=64, null=True, default=None, blank=True)
	item_component = models.ForeignKey(ComponentList, null=True, blank=True, default=None)
	item_justification = models.CharField(max_length=1024, null=True, default=None, blank=True)

def extract_tags(s):
	return s.split(' ')

class TechStack(models.Model):
	domain = models.CharField(max_length=128, null=True, default=None, blank=True)
	company_slug = models.SlugField(max_length=255, unique=True)

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

	@property
	def get_contributors(self):
		l=[]
		for c in self.contributors.all():
			l.append(c.get_name)
		return 

	@property
	def get_domain(self):
		return self.domain
	
	@property
	def get_company_description(self):
		return self.company_description

	@property
	def get_company_types(self):
		return extract_tags(self.company_type_of_application)

	@property
	def get_company_name(self):
		return self.company_name

	@property
	def get_company_slug(self):
		return self.company_slug
	
	@property
	def get_frontend_languages(self):
		return extract_tags(self.frontend_languages)

	@property
	def get_frontend_framework(self):
		return extract_tags(self.frontend_framework)

	@property
	def get_frontend_libraries(self):
		return extract_tags(self.frontend_libraries)
		
	@property
	def get_backend_languages(self):
		return extract_tags(self.backend_languages)

	@property
	def get_backend_framework(self):
		return extract_tags(self.backend_framework)

	@property
	def get_backend_libraries(self):
		return extract_tags(self.backend_libraries)

	@property
	def get_databases(self):
		return extract_tags(self.database)

	@property
	def get_server_configuration(self):
		return extract_tags(self.server_configuration)

	@property
	def get_server_ram(self):
		return self.server_ram

	@property
	def get_server_nodes(self):
		return self.server_nodes

	@property
	def get_server_hosting_provider(self):
		return extract_tags(self.server_hosting_provider)

	@property
	def get_server_description(self):
		return self.server_description

	@property
	def get_summary_tags(self):
		a=self.get_company_types
		a.extend(self.get_backend_languages)
		a.extend(self.get_backend_framework)
		a.extend(self.get_server_hosting_provider)
		return a

	@classmethod
	def get_featured_list(cls):
		return TechStack.objects.all()[:10]

@receiver(post_save, sender=TechStack)
def slugify_company_name(sender,instance,created,**kwargs):
    if created:
        instance.company_slug =  slugify(instance.company_name)
        instance.save()
