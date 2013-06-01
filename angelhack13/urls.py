from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'stack.views.landing', name='landing_page'),
    url(r'^register/', 'users.views.register'),

	# registration complete
	url(r'^register/complete/$',
	   direct_to_template,
	   {'template': 'registration/registration_complete.html'},
	   name='registration_complete'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
