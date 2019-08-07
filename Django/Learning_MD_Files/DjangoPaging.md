1. 原生切片实现分页：

        def get_students_page(request):
            info_num = int(request.GET.get('info_num'))
            page_num = int(request.GET.get('page_num'))
            print(info_num, page_num)
            students = Student.objects.all()[info_num*(page_num-1): info_num*page_num]
            return render(request, 'student_list.html', context={'students': students})
            
2. Django内置分页器： Paginator()

        def get_students_page2(request):
            per_page = int(request.GET.get('per_page', 10))
            page = int(request.GET.get('page', 1))           # url不指定参数时，第一个页面显示第一页
            students = Student.objects.all()

            paginator = Paginator(students, per_page)        # 分页器实例化（QueryList, per_page）
            page_object = paginator.page(page)               # 第（page）页的一个对象
            page_range = paginator.page_range                # 存储页码的列表 [页码]

            context = {
                'page_object': page_object,
                'page_range': page_range,
            }

            return render(request, 'student_list_generator.html', context=context)
            
3. Django内置分页器： Paginator()

    templates 中 url反向解析：
    分页器的实现，给url中加入 request.GET 可获取参数

        {% for page_index in page_range %}
        <li><a href="{% url 'get_student_page2' %}?page={{ page_index }}">{{ page_index }}</a></li>
        {% endfor %}
        
4.                         