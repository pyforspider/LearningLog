from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from App.models import Grade, Student, StuInfo


def get_grade(request):
	grades = Grade.objects.all()

	return render(request, 'grade_list.html', context=locals())


def get_students(request, g_id):
	students = Student.objects.filter(s_grade_id=g_id).filter(is_delete=0)   # s_grade_id 关联的是班级的id
	context = {
		'students': students,
		'g_id': g_id,
	}

	return render(request, 'student_list.html', context=context)


def get_info(request, stu_id):
	if Student.objects.get(pk=stu_id).is_delete == 0:
		s_infos = StuInfo.objects.filter(i_name_id=stu_id)     # i_name_id 关联的是学生的id
		return render(request, 's_info.html', context=locals())
	else:
		return HttpResponse("数据已删除")


def delete(request, s_id):
	student = Student.objects.get(pk=s_id)
	student.is_delete = 1
	student.save()
	return HttpResponse('删除成功')


def to_create_student(request, g_id):
	context = {
		'g_id': g_id,
	}

	return render(request, 'create_student.html', context=context)


def create_student(request, g_id):
	new_student_name = request.POST.get('newstudent')    # 先从表单中获取名字

	student = Student()
	student.s_name = new_student_name
	student.s_grade_id = g_id                       # 从学生列表的url中获取 g_id ，传递进来
	student.save()

	return HttpResponseRedirect('/app/getstudents/%s/' % g_id)
