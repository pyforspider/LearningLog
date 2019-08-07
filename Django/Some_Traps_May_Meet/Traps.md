1. 在Pycharm中导入Mysql数据库时：

    1. 时区问题
    命令行进入mysql修改时区为 +8:00

    2. Pycharm导入Mysql数据库
    在完成输入用户名、密码、数据库名后test connection，点击Apply后直接叉掉窗口，不要点击OK。否则数据库表导不进来
    
2. 查询结果时，写条件注意在属性后加双下划线‘__’:

        persons = Person.objects.exclude(p_age__lt=50).filter(p_age__lt=80)
        
        persons = Person.objects.order_by('-id')
        persons = Person.objects.all().order_by('-id') # all()可要可不要
        
        persons_values = persons.values() # values()是一个方法，用来获取查询集合里对象所有属性的键值对，返回一个由字典组成的列表。

    结果是一个QuerySet
    需要迭代for循环输出结果。加上对象的属性，如persons.s_name
    
3. 快捷键：

    * .re 快捷生成return
    * .if 多用点
    
4. 创建对象时可以用下面方法：

        person = Person().objects.create(p_name='', p_age= , ... )  # 所有属性都得写
        peson = Person(p_name='', p_age= , ... )                    # 所有属性都得写
    
    如果不写 p_name 则数据库保存的为''， 而非 None Null
    
5. 使用python manage.py shell 时：

        python manage.py shell

        user = User()
        user.o_num="119"        # 不能使用‘119’，否则数据库不显示
        
        