
from django.urls import path

from Two import views

urlpatterns = [
	path('getuser/', views.get_user),
	path('getusers/', views.get_users),
	path('getorder/', views.get_order),
	path('getgrade/', views.get_grade),
	path('getcustom/', views.get_custom),
	path('getcompany/', views.get_company),
	path('getanimals/', views.get_animals),
]