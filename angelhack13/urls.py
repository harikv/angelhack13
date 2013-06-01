from django.conf.urls import patterns, include, url
from stack.views import LandingPageView, CompanyPageView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', LandingPageView.as_view(), name='home'),
    url(r'^company/', CompanyPageView.as_view(), name='company_page'),
    # url(r'^angelhack13/', include('angelhack13.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
