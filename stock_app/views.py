from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

def	auth(request):
	form = UserCreationForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			data=form.cleaned_data
			username=data['username']
			password=data['password1']
			User.objects.create_user(username=username,password=password)
			return HttpResponseRedirect('stockapp/login')
		return render_to_response('sign_up.html',{'form':form},ci)
	else:
		ci=RequestContext(request)
		return render_to_response('sign_up.html',{'form':form},ci)
	
	
