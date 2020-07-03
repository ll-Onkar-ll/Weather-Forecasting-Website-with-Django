from django.contrib.auth import get_user_model
from django.db import models

class ProfilePic(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	pic = models.CharField(max_length=50)