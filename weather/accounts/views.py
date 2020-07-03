from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, views
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreateForm

def index(request):
	if request.method == "POST":
		if request.POST.get('submit') == 'signup':
			form_crt = UserCreateForm(request.POST)
			if form_crt.is_valid():
				form_crt.save();
				return redirect('/accounts/index')
			else:
				context = {
        				'form_crt': form_crt,
        				'flag': True,
    				}
				return render(request, 'registration/login.html', context)
		elif request.POST.get('submit') == 'login':
			return views.LoginView.as_view()(request)
	else:
		#return render(request, 'registration/login.html')
		return views.LoginView.as_view()(request)

def login(request):
	return redirect('login')