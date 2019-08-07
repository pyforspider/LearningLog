from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

from Three.models import Student, Grade


def index(request):
	three_index = loader.get_template('three_index.html')
	context = {
		'student_name': 'Sunck'
	}
	result = three_index.render(context=context)
	print(result)
	return HttpResponse(result)


# 从学生获取班级信息
def get_grade(request):
	student = Student.objects.get(pk=1)
	grade = student.s_grade.g_name

	return HttpResponse('Grade %s' % grade)


# 从班级获取学生信息
def get_students(request):
	grade = Grade.objects.get(pk=1)
	students = grade.student_set.all()
	context = {
		"students": students,
	}

	return render(request, 'student_three_list.html', context=context)
