from users.forms import HackerRegistrationForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.views import login as django_login
from emailusernames.forms import EmailAuthenticationForm

def login(request):
    if not request.user.is_authenticated():
        extra_context={}
        return django_login(request, template_name='registration/login.html', authentication_form=EmailAuthenticationForm, extra_context=extra_context)
    else:
        return redirect(reverse('landing_page'))

def register(request):
    if not request.user.is_authenticated():
        from registration.views import register
        return register(request, backend='registration.backends.default.DefaultBackend', form_class=HackerRegistrationForm, success_url=reverse('registration_complete'), template_name='registration/registration_form.html')
    else:
        #if logged in
        return redirect(reverse('landing_page'))

def activation_complete(request):
        return redirect(reverse('login'))
