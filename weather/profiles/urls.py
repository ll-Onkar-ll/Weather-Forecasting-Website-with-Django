from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
	path('profile/', login_required(views.profile), name='profile'),
]