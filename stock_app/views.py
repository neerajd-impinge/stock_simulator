from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from decimal import Decimal as d

import requests

def	auth(request):
	form = UserCreationForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			data = form.cleaned_data
			username = data['username']
			password = data['password1']
			user = User.objects.create_user(username=username,password=password)
			UserProfile.objects.create(user=user)
			return redirect('/stockapp/login')
		return render_to_response('sign_up.html',{'form':form},ci)
	else:
		ci=RequestContext(request)
		return render_to_response('sign_up.html',{'form':form},ci)

@login_required
def home(request):
	try:
		userProfile = UserProfile.objects.get(user = request.user)
	except :
		balance = None
		#return HttpResponse('something went wrong , please try again')
	comp = ['F','GE','JNJ']
	url = 'http://data.benzinga.com/stock/'
	data = {}
	i = 1
	for c in comp:
		data[i] = {}
		r = requests.get(url +str(c))
		data[i]['company'] = c
		data[i]['json'] = r.json()
		i = i + 1
	return render_to_response('home.html',{'data':data,'userProfile':userProfile}, RequestContext( request ) )

def viewCompany(request,company):
	url = 'http://data.benzinga.com/stock/'
	r = requests.get(url +str(company))
	data = r.json()
	return render_to_response('company_stock.html',{'data':data}, RequestContext( request ) )

def search(request):
	try:
		userProfile = UserProfile.objects.get(user = request.user)
	except :
		balance = None
		return HttpResponse('something went wrong , please try again')
	try:	
		c = request.GET['q']
	except Exception as e:
		c = None
	if c == '':
		messages.warning(request, 'you are searching for nothing ,Please submit some parameters for search.')
		return redirect('/') 
	url = 'http://data.benzinga.com/stock/'
	r = requests.get(url +str(c))
	data = r.json()
	return render_to_response('search.html',{'data':data,'userProfile':userProfile}, RequestContext( request ) )

def stockAction(request, action):
	if action == 'buy':
		p = request.POST['price']
		qty = request.POST['qty']
		price = int(qty) * d(p)
		userProfile = UserProfile.objects.get(user = request.user)
		avail_b = userProfile.available_balance
		if d(price) > (avail_b):
			messages.warning(request, 'You cureent balance is low so you cannot buy '+qty+' number of stocks')
			return redirect(request.META.get('HTTP_REFERER'))
		new_avail_balance = userProfile.available_balance - d(price)
		userProfile.available_balance = new_avail_balance
		userProfile.save()
		return redirect('/')
	if action == 'sell':
		p = request.POST['price']
		qty = request.POST['qty']
		price = int(qty) * d(p)
		userProfile = UserProfile.objects.get(user = request.user)
		new_avail_balance = userProfile.available_balance + d(price)
		userProfile.available_balance = new_avail_balance
		userProfile.save()
		return redirect('/')
	