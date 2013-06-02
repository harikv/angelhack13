from django.db import models
from django.contrib.auth.models import User
from registration.signals import user_registered

class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=True)

    class Meta:
        abstract = True

class Hacker(UserProfile):
	# position in company
    position = models.CharField(blank=False, null=False, max_length=200)

    def __unicode__(self):
        return self.get_name

    @classmethod
    def create_hacker(cls, sender, **kwargs):
        request, instance = kwargs['request'], kwargs['user']
        try:
        	position = request.POST['position']
        	cls(user = instance, position=position).save()
        except KeyError:
            #UserProfile(user = instance).save() #Default create just a profile
            pass

    @property
    def get_email(self):
        return self.user.email

    @property
    def get_name(self):
        return self.user.first_name+' '+self.user.last_name

user_registered.connect(Hacker.create_hacker)
