from django import forms
from stack.models import StackItem
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class StackItemForm(forms.ModelForm):
	class Meta:
		model = StackItem
	def __init__(self, *args, **kwargs):
        super(StackItemForm, self).__init__(*args, **kwargs)
	def clean(self):
		cleaned_data = super(StackItemForm, self).clean()
		#do form level validation here
		return cleaned_data
	