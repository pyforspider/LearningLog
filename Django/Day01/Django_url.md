1. 路由中捕获变量(对应视图函数需要加入此参数)：

    1、位置参数(这个就是关键字参数)：
    path('students/<s_id>/', views.student) # 关键字参数 
    path('students/<int:s_id>/', views.student) # int 声明类型，注意<int:s_id>之间不能有空格

    2、关键字参数
    关键字变量对于顺序不做要求
    
2. urls 反向解析：

    由于urls 容易经常变更，所以需要给他起个名字，在主路由里用‘’namespace‘’，在子路由中用‘’name‘’。

    1、<a href="/two/learn/">go go go</a>
    
    2 、<a href="{% url 'learn' %}">Go learning</a>
    
    第二种很奇怪，不需要主路由的namespace，直达子路由
    
    3、在有关键字捕获的路由中怎么用？
    
        path('getdate/<int:year>/<int:month>/<int:day>/', views.get_date, name='get_time')
        <a href="{% url 'get_time' 15 31 48 %}">Get time</a>
    
    就是在路由名字后面 追加 关键字的参数；
    另外一种：
    
        <a href="{% url 'get_time' month=45 year=15 day=48 %}">Get time</a>
    
    如果不指定关键字，则按顺序匹配，加上关键字顺序无所谓
    
        <a href="{% url 'student' grade.id %}">{{ grade.g_name }}</a>
    
    如果在{% %} 表达式中，不需要 {{ grade.id }}
    
3. 超链接问题：

    注意将所需点击的文字放在 <a> ... </a>内。
    
        <h3><a href="/app/">删除</a></h3>
        
4. Django urls.py 书写规则：

    Django出现'set' object is not reversible错误
    检查项目中的ruls.py文件是否把 urlpatterns 列表的 [] 写成了 {} 。 
    集合是无序的，所以报了不能逆转的错误。
    
5. urls命名捕获：

        path('getgoodslist/<int:customer_id>/', views.get_goods_list, name='get_goods_list'),