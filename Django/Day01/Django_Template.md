1. HTML for 语句 当索引的集合为空时： 

        {% for student in students %}
            <li>{{ student.get_student }}</li>
        {% empty %}
            <li>没有对应的学生</li>
        {% endfor %}
        
2. HTML计数器：

        {% for student in students %}
            <li>{{ forloop.counter }} : {{ student.s_name }}</li>
        {% empty %}
            <li>没有对应的学生</li>
        {% endfor %}

    除了counter, 还有counter0, revcounter, revcounter0, first, last 用来计数，也可以用来判断:

        {% if forloop.first %}
            <li style="color: red">{{ student.get_student }}</li>
        {% else %}
            <li style='color: blue'>{{ student.get_student }}</li>
        {% endif %}
        
3. HTML 注释：

    <-- ... --> 这种注释在网页上可以被看到
    所以改成一下两种：
    
        1.  {# ... #}
        2.  {% comment %}
            <li>xxx</li>
            {% endcomment %}
            
4. HTML 里的运算 和 整除

        {% withratio 数 分母 分子 %}
        {% withratio 15 3 2 %} 最终显示 10
        {% withratio 15 2 3 %} 最终显示 22.5
        
        '|' 管道或者过滤器，前者输出作为后者输入
        {% if num | divisiableby : 2 %} 

    例如： 
    
        {% for student in students %}
            {% if forloop.counter|divisibleby:2 %} # 使用计数器实现隔行变色
                <li style="color: red">{{ student.s_name }}</li>
            {% else %}
                <li style="color: blue">{{ student.s_name }}</li>
            {% endif %}
        {% endfor %}
        
5. HTML ifequal 

        {% ifequal value1 value2 %} 
        {% endifequal %}
        
        # 实现选取循环第5个结果
        {% ifequal forloop.counter 5 %} 
        
6. 过滤器 作用于变量属性

    {{ var | 过滤器 }}

        实例：
        {{ p.page | add: 5 }}
        {{ p.page | add: -5 }} # 没有decrease
        
        {{ p.name | lower }} 
        {{ p.name | upper }}
        
7. 过滤器可以传递参数

    参数用引号引起来： 

        {{ students | join '=' }}

    默认值 

        {{ var | default ‘value’ }}

    根据指定格式转换日期为字符串：
    
        {{ dateVaule | date: 'y-d-m' }}
        
8. HTML 转义

    如果 code里有html标签，正常显示标签，加上safe后渲染
        
        html : {{ code | safe }} 

    注意慎用safe：恶意用户注入入javascript代码，如：
    
        code = '''
        <h2>睡着了</h2>
        <script type="text/javascript"></script>
        alert('你的网站被攻陷了！')；
        </script>
        '''

9. HTML 多行转义 开关作用  if save

        {% autoescape off %} #HTML 语法， 用于多行
        code
        {% endescape %}
        
        {% autoescape on %} 
        code
        {% endescape %}
        
10. template 布局

    {% block var %}
    {% endblock %} 挖坑 用来规划布局 
    注意：继承了该页面的子页面HTML只能写在block模块内！！!
    
    首次出现，代表规划； 第二次出现，代表填坑； 第三次及以后出现， 代表覆盖，
    除非声明 {{ block super }} 。
    
    {% extends 'base.html' %} 继承模板,可以获得父模板中的所有结构
    
    block + entends 化整为零
    
11. template 布局2

    include 将页面作为一部分，嵌入其他页面中， 可以直接放在父模板里。
    
        {% bolck var %}
        {% include '...html' %}
        {% endblock %}

    include + block 由零聚一
    可以同extends 三者混合使用， 但是能用extend + block的尽量用这个，include效率低
    
12. HTML 中增加CSS样式

    1. setting里给出 STATICFILES_DIR = [BASE_DIR, '' ]
    2. 在父模板base.html 中挖坑，在所需子模板中填坑。注意，在初始父模板添加。
    <link rel="stylesheet" href="/static/css/home_mine.css">

    更好的版本:
    在继承{extends}后添加 {% load static %} 声明
    <link rel="stylesheet" href={% static "css/home_mine.css" %}>
    
13. 动静分离

    1、创建静态文件夹
    
    2、在settings中注册STATICFILES_DIRS =[]
    
    3、在模板中使用
    
    先加载资源 {% load static %}
    使用{% static ‘xxx’ %} xxx相对路径
    
    坑点：
    仅在debug模式使用
    以后需要自己单独处理
    
14. 防跨站攻击 Django {% csrf_token %}

    防止恶意注册，确保客户端是我们的客户端
    使用了cookie中的csrftoken进行验证，传输
    服务器发送给客户端，客户端将cookie获取，还要进行编码转换（数据安全），即cookie再一次被转换。
    
    防止脚本重复发送post请求。大量注册无用账号
    而爬虫一般是get。
    
    如何实现：
    
    在我们 存在{% csrf_token %}标签的页面中，响应会自动设置一个cookie，csrftoken
    当我们提交的时候，会自动验证csrftoken
    验证通过，正常执行以下流程，验证不通过，403
    
15. 