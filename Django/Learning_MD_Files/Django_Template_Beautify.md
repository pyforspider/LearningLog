1. 分页器显示优化：

    1. 通过 https://www.bootcdn.cn/ 找到Bootstrap的css，js 链接标签，找到jquery链接标签，复制到 html的 </head> 之前

    2. 通过 https://v3.bootcss.com/components/#pagination 找到相关组件，如分页。复制到body，使用之前的 循环的标签 代替里面的标签部分

    3. Enable 允许 (禁止) 下一页和上一页进行翻页
        改写2复制的内容，上一页下一页使用 <a href="{% url 'get_student_page2' %}?page={{ page_object.previous_page_number }}" 来替代 <a href="#" 。下一页同理。

    4. 使得第一页最后一页不能翻页，隐藏手图标
        对第3步的前一页和后一页的链接添加 if 条件，else 条件，endif 条件
        其中，else 内容与if 内容相同，只改变标签链接，如'#'，则优化了，不会报错

        标签使用

            <li></li>是用来包<a></a>标签的

    5. 隐藏手图标
        在第4.1步基础上，在所需隐藏的`<a>`标签的`<li>`中加入 `<li class='disable'>`

    6. 实现当前页面按钮突出显示
        对for循环里添加条件，`{% ifequal page_index page_object.number %} ` 对此<a>链接的<li>增加<li class="active">

    两个script标签都没用到。
    
2. 分页按钮美化步骤 3,4,5

        {% if page_object.has_next %}
            <li>
                <a href="{% url 'get_student_page2' %}?page={{ page_object.next_page_number }}" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                </a>
            <li>
                {% else %}
            <li class="disabled">
                <a href="#" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                </a>
            <li>
        {% endif %}
        
3. 分页按钮美化步骤 6

        {% for page_index in page_range %}
            {% ifequal page_index page_object.number %}
                <li class="active"><a href="{% url 'get_student_page2' %}?page={{ page_index }}">{{ page_index }}</a>
                </li>
            {% else %}
                <li><a href="{% url 'get_student_page2' %}?page={{ page_index }}">{{ page_index }}</a></li>
            {% endifequal %}
        {% endfor %}
        
4.                    