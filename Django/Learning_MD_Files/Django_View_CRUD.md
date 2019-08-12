1. 获取单个对象：

    * 获取单个对象，没有匹配对象会抛异常。同时存在多个对象也会异常。使用Try...Except...
        
            person = Person.objects.get(p_age = 20) 
    
    * 获取第一个或者最后一个对象，all()可加可不加:
        
            person = Person.objects.[all()].first()
            person = Person.objects.last() 
    
        另外，正常情况可以获取，但是如果排序太乱，隐藏BUG，可能是同一个值，需要进行排序

2. 查询集可以做切片，左闭右开，相当于SQL的limit和offset

        users = User.objects.all()[1:5] 

3. 方法count() /exist()用法： 确认唯一性

    def get_user(request):
    
        username = 'Sunck'
        password = '120'
        
        users = User.objects.filter(u_name=username)
        
        if users.count():
            user = users.first()
                if user.u_password == password:
                    print('用户信息获取成功')
                else:
                    print('密码错误')
        else:
            print('用户不存在')

    可用于用户系统，确定唯一性
    
4. filter, exclude, all() 

    特性：都不会正在去查询， 只有迭代或者获取单个结果时，才会去查，懒查询模式。
    
    查询条件：属性__运算符=值，例如: u_age__gt=18 gt, lt, gte, lte, 
    in 在某一个集合里 filter(pk__in=[2, 4, 6, 8])
    
    contains 类似于模糊查询 like
    startswith 本质 like
    endswith
    exact 
    前面同时添加i，ignore忽略大小写iexact, istartswith, iendwith, icontains
    
5. 查询时间：

    year, month, day, week, hour, minute, second
    
        filter(lasttime__year=2017)
    
    定义模型时：
    
        order_time = models.DateTimeField(auto_now_add=True)
        
        orders = Order.objects.all().filter(o_time__month=9)
    查询时存在时区问题
    解决方法：
    1. 关闭Django里的时区表 settings.py --> USE_TZ = False
    2. 在数据库中创建对应的时区表
    
6. 跨关系查询：
 
    例如需要 根据学生查询其所在班级
    
    模型类名__属性名__比较运算符:
    
        # 此处 student 是Student类的小写
        grade = Grade.objects.all().filter(student__s_name='Jack')
    
    两种查询：正反查询 (通过 url 捕获的 g_id ):
    
        # s_grade_id 数据表自动生成
        students = Student.objects.all().filter(s_grade_id=g_id) 
        students = Grade.objects.get(pk=g_id).student_set.all()
        students = Grade.objects.get(s_grade=grade, )              # grade为Grade对象, 同时还可以增加其他条件，如s_name=...
        
7. 聚合函数 (Avg, Count, Max, Min ,Sum)

    使用aggregate() 返回聚合函数的值, 注意大写 需要alt+enter导包
    
        result = Student.objects.aggregate(Sum('s_age'))
    
    返回的是一个字典{ 's_age__sum' : 10 }
    
8. F和Q对象
    
    可以使用模型的A属性和B属性进行比较, 需要导入该F模块
    
        grades = Grade.objects.filter(ggirlnum__gt=F('gboynum'))
    
    F对象支持逻辑运算
    
        grades = Grade.objects.filter(ggirlnum__gt=F('gboynum') + 10 )
        
    Q对象：
    
    过滤器方法中的关键参数，用于组合条件: & (和) | (或) ~ (非)
        
    年龄小于25
    
        Students.objects.filter(Q(s_age__lt=25))
        companies = Company.objects.filter(Q(c_boy_num__gt=1) & Q(c_girl_num__gt=20))
        
9. 隐形属性： 

    作用可以增量修改筛选条件，只需要把下面的注释掉
    
        objects = models.Manager() #Manager类的一个实例

    super()函数为了将子类和父类关联起来，也可以写简写为`super().get_queryset().filter(is_delete=True)`
        
        class AnimalManager(models.Manager):
            def get_queryset(self): #重新父类实现all()的方法
                return super(AnimalManager, self).get_queryset().filter(is_delete=True)        
    
            此处使用model()方法创建了一个Manager实例对象:
            def create_animal(self):
                a = self.model() 
                a.a_name = a_name
                return a      
                
10.   
