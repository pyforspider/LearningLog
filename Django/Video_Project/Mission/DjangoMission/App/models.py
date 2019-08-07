from django.db import models


# Create your models here.
class Grade(models.Model):
	g_name = models.CharField(max_length=16, unique=True)


class Student(models.Model):
	s_name = models.CharField(max_length=32, unique=True)
	s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
	is_delete = models.BooleanField(default=False)


class StuInfo(models.Model):
	i_name = models.ForeignKey(Student, on_delete=models.CASCADE)
	i_hobby = models.CharField(max_length=16, default='gaming')
	i_age = models.IntegerField(default=18)
	i_birth = models.DateTimeField(auto_now_add=True)
