from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext


from django.contrib.auth.forms import UserCreationForm

def	auth(request):
	ci=RequestContext(request)
	return render_to_response('sign_up.html',{'form':UserCreationForm()},ci)
