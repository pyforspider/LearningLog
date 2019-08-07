1. 模型继承情况1：

        class Animal(models.Model):
            a_name = models.CharField(max_length=16)
    
        class Cat(Animal):
            c_food = models.CharField(max_length=32)
    
        class Dog(Animal):
            d_legs = models.IntegerField(default=4)

    此种继承Animal 表正常， 其余两表的主键字段变更为 animal_ptr_id 为 Animal自动生成的主键值

        def add_dog(request):
            dog = Dog()
            dog.a_name = 'Dog1'
            dog.save()
            return HttpResponse('Dog创建成功 %s' % dog.id)

        def add_cat(request):
            cat = Cat()
            cat.a_name = 'Cat1'
            cat.c_food = 'fish'
            cat.save()
            return HttpResponse('Cat创建成功 %s' % cat.id)

    数据获取：
    
        def get_dog(request):
            dog = Dog.objects.get(animal_ptr_id=11) # 如果用get(pk=1) 报错，因为不是自动生成pk的
            print(dog.a_name)
            return HttpResponse('获取成功')

    创建猫和狗时，在Animal表中同时创建，其主键id为 子类id主键值
    由于关系型在庞大数量后，查找变慢，因此不适应这种继承。
    
2. 模型继承 之 改进：

        class Animal(models.Model):
            a_name = models.CharField(max_length=16)
    
            class Meta:
                abstract = True
    
        class Cat(Animal):
            c_food = models.CharField(max_length=32)
    
        class Dog(Animal):
            d_legs = models.IntegerField(default=4)

    特点：
    使模型抽象化，抽象的模型就不会在数据库中生成映射，子模型映射出来的表直接包含父模型包含的字段

    使用场景：
    用户具有多个身份的时候
    
3. 在企业开发中：

    1. model --> sql
    都可以使用

    2. sql --> model
    django也提供了很好的支持

    步骤：
    首先，创建一个数据库，其次在新建项目命令行里输入：python manage.py inspectdb
    其次，删除App里的models.py
    最后，在命令行输入： python manage.py inspectdb > App/models.py

    注意：
    1. 直接根据数据表生成模型，元信息中包含 managed=False
    2. 如果自己的模型不想被迁移，managed=False 进行声明 
    
4.    
    