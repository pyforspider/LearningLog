from django.urls import path

from Two import views

urlpatterns = [
	path('students/', views.students),
	path('students/<int:s_id>/', views.student),
	path('getgrades/', views.get_grades),
	path('getstudents/<int:g_id>/', views.get_students),
	path('getdate/<int:year>/<int:month>/<int:day>/', views.get_date, name='get_time'),
	path('learn/', views.learn, name='learn'),
	path('haverequest/', views.have_request),
	path('createstudent/', views.create_student),
	path('getusername/', views.get_username, name='username'),
]