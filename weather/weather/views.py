from django.shortcuts import render, redirect
from profiles.models import ProfilePic
from django.contrib.auth.models import User
from .forms import LocationForm

import requests

def home(request):
	username = request.user.username
	user = User.objects.get(username=username)
	pp = ProfilePic.objects.filter(id=user.id)
	try:
		pp = ProfilePic.objects.get(user_id=user.id)
		pic = pp.pic
		pth = "submissions/" + username + "/"
		pth = pth + pic
	except ProfilePic.DoesNotExist:
		pth = "imgs/wet.png"
	return render(request, 'home.html', {'usr': username, 'fn': pth})

def prediction(request):
	username = request.user.username
	user = User.objects.get(username=username)
	try:
		pp = ProfilePic.objects.get(user_id=user.id)
		pic = pp.pic
		pth = "submissions/" + username + "/"
		pth = pth + pic
	except ProfilePic.DoesNotExist:
		pth = "imgs/wet.png"
	if request.method == "POST":
		if request.POST.get('submit') == 'getPrediction':
			formp = LocationForm(request.POST)
			if formp.is_valid():
				query = formp.cleaned_data['city']
				response = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=%s&units=metric&appid=9d7b748ab7d47e8f73a824885e4e69d2' % query)
				pred = response.json()
				context = {'pred': pred, 'res': response.text, 'usr': username, 'fn': pth}
				return render(request, 'prediction.html', context)
	return redirect('home')