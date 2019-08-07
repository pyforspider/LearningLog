from django.db import models


# Create your models here.
class Student(models.Model):
	s_name = models.CharField(max_length=64)
	s_age = models.IntegerField(default=1)
	# objects = models.Manager()
