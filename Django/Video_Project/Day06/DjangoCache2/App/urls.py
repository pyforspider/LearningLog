from django.urls import path

from App import views

urlpatterns = [
	path('index/', views.index, name='index'),
	path('news/', views.news, name='news'),
	path('jokes/', views.jokes, name='jokes'),
	path('getxm/', views.get_xm, name='get_xm'),
	path('getphone/', views.get_phone, name='get_phone'),
	path('getticket/', views.get_ticket, name='get_ticket'),
	path('search/', views.search, name='search'),
	path('calc/', views.calc, name='calc'),
	path('login/', views.login, name='login'),

	path('addstudents/', views.add_student, name='add_student'),
	path('getstudents/', views.get_students, name='get_student'),
	path('getstudentspage/', views.get_students_page, name='get_student_page'),
	path('getstudentspage2/', views.get_students_page2, name='get_student_page2'),

	path('getcode/', views.get_code, name='get_code'),

]
