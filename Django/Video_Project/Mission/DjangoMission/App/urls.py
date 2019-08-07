from django.urls import path

from App import views

urlpatterns = [
	path('getgrade/', views.get_grade),
	path('getstudents/<int:g_id>/', views.get_students, name='student'),
	path('getinfo/<int:stu_id>/', views.get_info, name='info'),
	path('delete/<int:s_id>/', views.delete, name='delete'),
	path('tocreatestudent/<int:g_id>/', views.to_create_student, name='to_create_student'),
	path('createstudent/<int:g_id>/', views.create_student, name='create_student'),
]
