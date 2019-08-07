from django.db import models


class User(models.Model):
	u_name = models.CharField(max_length=16)
	u_password = models.CharField(max_length=128)
	u_token = models.CharField(max_length=128)
