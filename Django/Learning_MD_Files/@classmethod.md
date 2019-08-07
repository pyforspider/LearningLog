#有什么用处？

####在继承类时，由于父类的__init__方法已经实现，所以子类不能实现__init__方法，否则重写父类方法。因此可以用如下方法：
    
    class Person(models.Model):
        p_name = models.CharField(max_length=16, unique=True)
        p_age = models.IntegerField(default=18)
        p_sex = models.BooleanField(default=False, db_column='sex')
        p_hobby = models.CharField(max_length=32, null=True, blank=True)

        @classmethod
        def create(cls, p_name, p_age=100, p_sex=True, p_hobby='gaming'):
            return cls(p_name=p_name, p_age=p_age, p_sex=p_sex, p_hobby=p_hobby)
            
####来重新创建子类实例，重新定义子类属性默认值。
