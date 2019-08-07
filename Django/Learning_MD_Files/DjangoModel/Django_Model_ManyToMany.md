1. Django模型之 多对多

    1. 开发中最复杂
    
    2. 开发中很少直接用多对多属性，而是自己维护多对多的关系
    
    3. 产生表的时候会产生单独的关系表
    3.1 关系表中存储关联表的主键，是通过多个外键实现的
    3.2 多个外键值不能同时相等，即不能出现a,b 之后还有 a,b
    
2. Django模型 之多对多 绑定：

        def add_to_cart(request):
            customer = Customer.objects.last()
            goods = Goods.objects.last()
            print(type(goods.g_customer))
            goods.g_customer.add(customer)
            return HttpResponse('绑定成功')

    注意： 由于是多对多的关系， goods.g_customer 存储的是一组customer，其类别是ManyRelatedManger, 所以在绑定时使用 goods.g_customer.add(customer) add()的方法来绑定

    此外，ManyRelatedManger是函数中定义的类，并且父类是一个参数，动态创建
    方法： add(), remove(), clear(), set()
    
3. Django模型 之多对多 级联数据获取：QuerySet Manage对象，支持all(), filter(), exclude()....

    从获取主：
    使用属性，属性是一个Manage子类
    
        goods.g_customer.add(customer)
    
    除了add，还有remove， clear， set

    主获取从：
    隐形属性，也是Manage子类，操作和从操作主完全一样
    
        customer.goods_set.add(goods)
        
4. Django模型 之多对多 级联数据获取：QuerySet

        def get_goods_list(request, customer_id):
            customer = Customer.objects.get(pk=customer_id)
            goodslist = customer.goods_set.all()
            for goods in goodslist:
                print(goods.g_name)
            return HttpResponse('获取成功') 
            
5. 模型多对多实际应用中：

    不使用ManyToManyField
    通常自己创建一个表Cart(models.Model)，含有以下属性

        customer_id = model.Foreignkey(Custom)
        goods_id = model.Foreignkey(Goods)
        goods_num = model.CharField()
        is_select = model.BooleanField()                   