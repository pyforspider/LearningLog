from django.urls import path

from Two import views

urlpatterns = [
	path('index/', views.index, name='index'),
	path('login/', views.login, name='login'),
	path('mine/', views.mine, name='mine'),
	path('logout/', views.logout, name='logout'),
	path('register/', views.register, name='register'),
	path('userlogin/', views.user_login, name='user_login'),
	path('usermine/', views.user_mine, name='user_mine'),
]