1. 绘画验证码三种材料：

        image = Image.new(mode=mode, size=size, color=color)         # 画布
        image_drew = ImageDraw(image, mode=mode)                     # 画笔
        image_font = ImageFont.truetype(settings.FONT_PATH, 90)      # 设置 字体
        
2. 开始绘画：

        text = generate_code()
        for i in range(4):
            fill = get_rgb_tuple()
            image_drew.text(xy=(50*i, 0), text=text[i], font=image_font, fill=fill)	    # 用画笔画字
        for i in range(10000):
            fill = get_rgb_tuple()
            image_drew.point(xy=(random.randrange(0, 200), random.randrange(0, 100)), fill=fill)
            
3. 画完之后以流形式存储，并提交给响应，客户端使用image/png解析

        fp = BytesIO()
        image.save(fp, 'png')
        
        return HttpResponse(fp.getvalue(), content_type='image/png')
        
4. 验证;

    在get_code()里通过：

        code = generate_code()
        request.session['code'] = code # 获得code后进行session设置

    然后在login()进行验证：

        elif request.method == 'POST':
        code = request.POST.get('verifycode')    # 从网页表单获取验证码
        code_s = request.session.get('code')     # 从session里提取code，进行比对
        if code == code_s:
            return HttpResponse('POST登录成功')
        else:
            return HttpResponse('POST登录失败')
            
5. HTML 给验证码 添加点击事件：

    1. head加上jquery.js：
    
            <script type="text/javascript" src="https://cdn.bootcss.com/jquery/1.11.1/jquery.js"></script>

    2. 顶部加载
    
            {% load static %}

    3. head加上
            
            <script type="text/javascript" src="{% static 'js/login.js' %}"></script>
            
6. login.js文件：

    由于只有地址变化了图片才会变化:
    
        $(function () {
            $("img").click(function () {
                console.log("点到我了");
                $(this).attr("src", "/app/getcode/?t=" + Math.random());   
               
            })
        })
        
7.       