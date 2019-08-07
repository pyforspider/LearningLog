from django.http import HttpResponse
from django.shortcuts import render

from Two.models import Grade, Student


def students(request):
	return HttpResponse('响应成功.')


def student(request, s_id):
	print(s_id)
	print(type(s_id))
	return HttpResponse('Http response success.')


def get_grades(request):
	grades = Grade.objects.all()
	return render(request, 'grade_list.html', context=locals())


def get_students(request, g_id):

	# students = Student.objects.all().filter(s_grade_id=g_id)  # s_grade_id 数据表自动生成
	students = Grade.objects.get(pk=g_id).student_set.all()

	# print(students)
	# return HttpResponse('正在调试')

	return render(request, 'get_students.html', context=locals())


def get_date(request, day, year, month):
	return HttpResponse("Time: %s : %s : %s " % (year, month, day))


def learn(request):

	return HttpResponse("love learning.")


def have_request(request):

	meta = request.META
	for met in meta:
		print(met, '                              ', meta[met])
	print(request.GET.getlist('hobby'))

	return HttpResponse("获取成功")


def create_student(request):
	return render(request, 'creat_student.html')


def get_username(request):

	username = request.POST.get('username')

	return HttpResponse(username)
