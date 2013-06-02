from emailusernames.forms import EmailAuthenticationForm, EmailUserCreationForm
from django.contrib.auth.models import User
from django import forms

class HackerRegistrationForm(EmailUserCreationForm):
    """
    Email Registration Form

    This is a custom Email Registration form that inherits EmailUserCreationForm from
    emailusernames to make it compatible with django-registration

    See https://github.com/dabapps/django-email-as-username/issues/17

    Since django-registration's register view expects a username argument, we pass it in here
    
    """
    first_name = forms.CharField()
    last_name = forms.CharField()
    position = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(HackerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['first_name', 'last_name', 'position', 'email', 'password1', 'password2']
    
    def clean_email(self):
        """
        Check the supplied email address against a list of known free
        webmail domains.
        
        """    	
    	bad_domains = ['aim.com', 'aol.com', 'email.com', 'gmail.com',
                   'googlemail.com', 'hotmail.com', 'hushmail.com',
                   'msn.com', 'mail.ru', 'mailinator.com', 'live.com',
                   'yahoo.com']

        email_domain = self.cleaned_data['email'].split('@')[1]
        
        if email_domain in bad_domains:
            raise forms.ValidationError(("Please sign up with your company email address."))

        email = self.cleaned_data["email"]
        from emailusernames.utils import user_exists
        if user_exists(email):
            raise forms.ValidationError(("A user with that email already exists."))

        return self.cleaned_data['email']

    def clean(self):
        cleaned_data = super(HackerRegistrationForm, self).clean()
        if cleaned_data.has_key('email'):
            cleaned_data['username'] = cleaned_data['email']
        return cleaned_data
