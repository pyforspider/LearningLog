from django.urls import path

from Two import views

urlpatterns = [
	path('index/', views.index),
	path('addstudent/', views.add_student),
	path('getstudents/', views.get_students),
	path('updatestudent/', views.update_student),
	path('deletestudent/', views.delete_student)
]