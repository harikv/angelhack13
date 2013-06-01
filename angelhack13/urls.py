from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from stack.views import LandingPageView, CompanyPageView
from django.contrib.auth import views as auth_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	# registration complete
	url(r'^register/complete/$',
	   direct_to_template,
	   {'template': 'registration/registration_complete.html'},
	   name='registration_complete'),

    # Examples:
    url(r'^register/', 'users.views.register', name='register'),

    # login
        url(r'^login/$', 'users.views.login', name='login'),
                
    # logout
        url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    # registration complete
    url(r'^register/complete/$',
           direct_to_template,
           {'template': 'registration/registration_complete.html'},
           name='registration_complete'),

        url(r'^activate/complete/$',
        direct_to_template,
        {'template': 'registration/activation_complete.html'},
        name='seller_registration_activation_complete'),

    #custom view for activation completion to display right login page (seller vs buyer)
    url(r'^activate/complete/$',
                           'users.views.activation_complete',
                           name='registration_activation_complete'),

    (r'', include('registration.backends.default.urls')),

    url(r'^$', LandingPageView.as_view(), name='landing_page'),
    url(r'^company/', CompanyPageView.as_view(), name='company_page'),
    url(r'^newstack/', 'stack.views.CreateStackForm', name='new_stack'),
    # url(r'^angelhack13/', include('angelhack13.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'stack.views.index'),
#    url(r'^submit/(?P<component>\d)/$', 'stack.views.submit'),
)
