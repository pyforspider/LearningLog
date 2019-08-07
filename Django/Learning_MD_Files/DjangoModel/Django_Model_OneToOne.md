1. 在定义模型时，关联外键：

        s_grade = models.Foreignkey(Grade, on_delete=models.CASCADE)
        
2. HTML挖坑既可以调用对象的属性，也可以调用对象的方法。

        class Student(models.Model):
            s_name = models.CharField(max_length=16)
        
            def get_student(self):
                return self.s_name
    
    还可以通过索引： students.0.s_name
    
    还可以传字典： student_dict.hobby # 似乎不能for迭代，只能通过属性查询
    
3. 构建模型情况1：

    原先：

        class Student(models.Model):
            s_name = models.CharField(max_length=16)
        已完成迁移makemigrations， migrate

    后新增：

        class Student(models.Model):
            s_name = models.CharField(max_length=16)
            s_age = models.IntegerField(default=1)

        class Grade(models.Model):
            g_name = models.IntegerField(max_length=16)

    则应该先1、删除迁移文件，2、对应数据库表，3、以及数据库表django_migrations中对应的记录
     
    注意：仅删除App 中相关记录 0001_initial， session的0001_initial不能删
    
4. 模型构建情况2：

    已有Student， Grade 模型，
    新增一个School 模型，makemigrations后会生成一个新的迁移文件，0002_school。

    0002_school 依赖于第一个迁移文件：
    
        dependencies = [
        ('App', '0001_initial'),
        ]
        
5. 迁移模型：

    python manage.py makemigrations
    
    python manage.py makemigrations app-name # 为指定app迁移模型
    
    python manage.py makemigrations --help 查看迁移相关帮助
    
    python manage.py --help 查看帮助
    
6. 模型一对一：

        class Person(models.Model):
            p_name = models.CharField(max_length=16)
            p_sex = models.BooleanField(default=False)

        class IDCard(models.Model):
            id_num = models.CharField(max_length=18, unique=True)
            id_person = models.OneToOneField(Person, on_delete=models.CASCADE, null=True, blank=True) 
            
    一对一迁移后，表中一个是 id_num ，另一个是 id_person_id， 注意设置可空，否则新增IDCard实例时失败报错。
    
    如果之前忘记加了null=True，继续加上再迁移就行

    先创建两个视图函数，通过GET url中的参数获得值，add_person(request)，add_idcard(request)，创建实例对象，在通过函数 bind_card 一对一绑定卡

        def bind_card(request):
            person = Person.objects.last()
            idcard = IDCard.objects.last()
            idcard.id_person = person
            idcard.save()
            return HttpResponse('绑定成功')
            
7. 模型一对一 之绑定：

    第二种情况：
        已有一个person和一个idcard，再创建一个person，能通过绑定成功吗？结果怎样？
        可以绑定成功， id_person_di 会变成 2

    第三种情况：
        已有一个person，一个idcard，再创建一个idcard，能将新idcard绑定之前的person吗？
        不能，报错。

    结论：谁声明一对一关系，谁就不能有 “第三者“ 对之前的对象进行绑定。
    
8. 模型一对一 总结：

    1. 应用场景
    用于复杂表的拆分
    扩展新功能

    2. Django中的OneToOneField
    使用的时候，关系声明还是有细微差别的

    3. 实现
    使用外键实现？ Django 1.9.11
    对外键添加了唯一约束？ 理解： 原本idcard对应很多person，但是对应其他person的线被约束了。

    4. 数据删除
    级联表 主表 从表 谁声明关系谁就是从表
    在开发中确认主从：留主删从，一般用户是主表

    5. 默认特性（CASCADE）
    从表数据删除， 主表不受影响
    主表数据删除，从表一起删除

    6. 其他特性
    models.PROTECT： 再删除主表内对象时会发生报错，只有删除从表相关数据才能删除， 开发中为防止误操作，通常设置此模式
    models.SET_NULL ： 删除主表中数据时，从表中的值设为null。一对一绑定只能设置此模式，不能default。否则idcard相同
    models.SET_DEFAULT ： 设为default中的值
    models.SET() ：自定义值
    
9. 模型一对一 之 数据删除：

    idcard 第一条数据绑定了people，第二条数据没有绑定people
    当执行：

        def remove_idvard(request):
            id_card = IDCard.objects.last()
            id_card.delete()
            return HttpResponse('身份证移除成功')
        第一次，第二次均移除成功。

    person 第一条数据没有绑定idcard，第二条数据绑定了idcard（idcard只有一条数据）

    当执行：

        def remove_person(request):
            person = Person.objects.last()
            person.delete()
            return HttpResponse('人员移除成功')

    移除成功，且相关联的idcard也删除了，因为有 on_delete = models.CASCADE
    如果 on_delete = models.SET_NULL ，则id_card不会被删除，且设置为null 
    
10. 模型一对一 之 获取数据：

        def get_idcard(request):
            person = Person.objects.last()
            idcard = person.idcard                # idcard隐形属性 即模型名称小写 
            return HttpResponse(idcard.id_num)

        def get_person(request):
            idcard = IDCard.objects.last()
            person = idcard.id_person
            return HttpResponse(person.p_name)
            
11.                           