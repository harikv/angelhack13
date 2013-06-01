from users.forms import HackerRegistrationForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

def register(request):
    if not request.user.is_authenticated():
        from registration.views import register
        return register(request, backend='registration.backends.default.DefaultBackend', form_class=HackerRegistrationForm, success_url=reverse('registration_complete'), template_name='registration/registration_form.html')
    else:
        #if logged in
        return redirect(reverse('landing_page'))