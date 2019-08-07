from django.db import models


# Create your models here.
class User(models.Model):
	u_name = models.CharField(max_length=16, unique=True)
	u_password = models.CharField(max_length=256)
	objects = models.Manager()


class Order(models.Model):
	o_num = models.CharField(max_length=16, unique=True)
	o_time = models.DateTimeField(auto_now_add=True)
	objects = models.Manager()


class Grade(models.Model):
	g_name = models.CharField(max_length=16)
	objects = models.Manager()


class Student(models.Model):
	s_name = models.CharField(max_length=16)
	s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
	objects = models.Manager()


class Custom(models.Model):
	c_name = models.CharField(max_length=16)
	c_cost = models.IntegerField(default=10)
	objects = models.Manager()


class Company(models.Model):
	c_name = models.CharField(max_length=16)
	c_girl_num = models.IntegerField(default=5)
	c_boy_num = models.IntegerField(default=3)


class AnimalManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(is_delete=False)

	def create_animal(self, a_name='Chicken'):
		a = self.model()  # 此处使用model()方法创建了一个Manager实例对象
		a.a_name = a_name
		return a


class Animal(models.Model):
	a_name = models.CharField(max_length=16)
	is_delete = models.BooleanField(default=False)
	objects = AnimalManager()



