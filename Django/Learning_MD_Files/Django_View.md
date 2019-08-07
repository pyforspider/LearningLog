1. 模板渲染：
    
    第一种：
    
        def index(request):
        content = loader.render_to_string('index.html')
        return HttpResponse(content)
        
    就是先loader，再渲染到字符串类型，返回Http响应
    
    第二种：可以在render()中传递参数context
    
        temp = loader.get_template('index.html')
        content = temp.render()
        return HttpResponse(content)
        
2. 模板语法填写变量： 

        class Grade(models.Model):
        g_name = models.CharField(max_length=16)
        
        class Student(models.Model):
        s_name = models.CharField(max_length=16)
        s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    实现根据班级找到所有对应的学生：

    grade.id 是数据表自动生成的
    找出所有的班级， 
    
        <li><a href='/two/getstudents/{{ grade.id }}/' {{ grade.g_name }} </a></li> 
        
    s_grade_id 是系统生成的(1,2,3)， g_id 是从url中捕获的
    
        students = Student.objects.all().filter(s_grade_id=g_id)
        
3.  Views视图函数双R之： Request对象

    def get_students(request):
    这个request 是一个由Djiango提供的HttpRequset对象，属性有path，method，GET，POST， method等参数
    
    例子：http://127.0.0.1:8000/two/haverequest/?hobby=coding&hobby=eating&hobby=sleeping
    
        request.Get 返回： <QueryDict: {'hobby': ['coding', 'eating', 'sleeping']}>
    
    返回的是一个类字典结构，迭代对象，其key允许重复。
    
        hobby = request.GET.get('hobby') --> sleeping
        hobbies = request.GET.getlist('hobby') --> ['coding', 'eating', 'sleeping']
        
4. 返回render()时，如：

        return render(request, 'student_list.html', context=context)

    如果 'student_list.html' 里有：
    
        <li><a href="{% url 'info' student.id %}">{{ student.s_name }}</a></li>
        {% endfor %}
        <h4><a href="{% url 'to_create_student' g_id %}">点击添加学生</a></h4>

    其中变量 student.id 和 g_id， 则必须在context中传过去。
    
5. 关于重定向问题：

        return HttpResponseRedirect('/app/getstudents/%s/' % g_id)

    返回的路径必须 '/' 开头，否则报错
    
6. 关于Response对象：

    属性：

        response = HttpResponse()
        reponse.content = "德玛西亚"
        response.status_code = 404
        response.charset = utf-8
        response.content-type = text/html

    方法：

        response.write('该刷马桶了')
        response.flush()

        return response
        
7. Response重定向问题：

    第一种：return HttpResponseRedirect('/app/hello/') #注意最前面的‘/’一点要有

    使用反向解析：

        url = reverse('hello')
        第二种：return HttpResponseRedirect(url)

        第三种简写：return redirect(url)
        
8. Reponse子类 JsonResponse:

    同于给移动端的json，给ajax

        def get_info(request):
        
        info = {
        'status': 200,
        'msg': 'ok',
        }

        return JsonResponse(info)
        
9. HttpResponse 子类:

        HttpResponseRedirect:
        重定向，暂时的，302，简写 redirect( )
        
        JsonResponse:
        以json形式返回数据，重写__init__，序列化json数据，指定content-type： application/json
        
        HttpResponsePermanentRedirect：
        重定向，永久性的，301 

        HttpResponseBadRequest(HttpResponse):
        status_code = 400
        
        HttpResponseNotFound(HttpResponse):
        status_code = 404
        
        HttpResponseForbidden(HttpResponse):
        status_code = 403
        
        HttpResponseNotAllowed(HttpResponse):
        status_code = 405
        
        HttpResponseServerError(HttpResponse):
        status_code = 500
        
        Http404(Exception):
        pass
        raise 主动抛异常   
        
10. 注意多个变量进行格式化时，需要加括号

        def get_date(request, year, month, day):
            return HttpResponse("Time: %s : %s : %s " % (year, month, day)     