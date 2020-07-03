from django.urls import path

from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
	path('index/', views.index, name='login'),
	path('login/', views.login),
]