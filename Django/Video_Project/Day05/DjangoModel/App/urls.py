from django.urls import path

from App import views

urlpatterns = [
	path('hello/', views.hello, name='index'),
]