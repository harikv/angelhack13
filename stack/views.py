# Create your views here.
from django.http import HttpResponse

def landing(request):
	return HttpResponse('Landing Page')