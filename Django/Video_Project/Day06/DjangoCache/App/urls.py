from django.urls import path

from App import views

urlpatterns = [
	path('hello/', views.hello, name='hello'),
	path('news/', views.news, name='news'),
]
