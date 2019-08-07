from django.urls import path

from Three import views

urlpatterns = [
	path('index/', views.index),
	path('getgrade', views.get_grade),
	path('getstudents', views.get_students),
]

