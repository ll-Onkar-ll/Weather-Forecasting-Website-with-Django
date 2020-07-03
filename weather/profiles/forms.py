from django import forms
from django.forms import ModelForm
from profiles.models import ProfilePic

class ProfilePicForm(ModelForm):
    file = forms.FileField()
    class Meta:
        model = ProfilePic
        exclude = ['user', 'pic']