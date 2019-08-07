1. 在定义模型时，关联外键：

        s_grade = models.Foreignkey(Grade, on_delete=models.CASCADE)
        
2. HTML挖坑既可以调用对象的属性，也可以调用对象的方法。

        class Student(models.Model):
            s_name = models.CharField(max_length=16)
        
            def get_student(self):
                return self.s_name
    
    还可以通过索引： students.0.s_name
    
    还可以传字典： student_dict.hobby # 似乎不能for迭代，只能通过属性查询
    
3. 