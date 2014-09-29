from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

def	auth(request):
	form = UserCreationForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			data=form.cleaned_data
			username=data['username']
			password=data['password1']
			user=User.objects.create_user(username=username,password=password)
			UserProfile.objects.create(user=user)
			return redirect('stockapp/login')
		return render_to_response('sign_up.html',{'form':form},ci)
	else:
		ci=RequestContext(request)
		return render_to_response('sign_up.html',{'form':form},ci)
	
	
