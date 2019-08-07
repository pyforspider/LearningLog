1. 创建静态文件路径：

    在 setting.py 文件中添加：
    
        STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'), #不要加斜杠
        ]

    可以在static中存储 img，css，js，html等等，html不会被渲染，页面效率高

    注意：主路径的templates 叫模板，支持模板语言和模板语法
    
2. 图片上传：

    表单：

        <form action="{% url 'upload_file' %}" method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <span>请上传文件</span><input type="file" name="image">
        <button name="submit">上传</button>
        {# <br>#}
        {# <input type="submit" value="上传">#}
        </form>

    接收：

        elif request.method == 'POST':
            image = request.FILES.get('image')
            print(type(image))
            with open('E:\\pyforspider\\mywebsite\\Day05\\SqlToModel\\static\\img\\picture.jpg', 'wb') as fb:
            for part in image.chunks():
            fb.write(part)
            fb.flush()
            return HttpResponse('上传成功')
            
    先chunks()切碎，写入，冲刷
    
3. 图片上传简洁版：

    1. 建立模型，加入

            class UserModel(models.Model):
                u_name = models.CharField(max_length=16)
        
                u_icon = models.FileField(upload_to='static')

        upload_to 相对路径， 相对于的是MEDIA_ROOT, 媒体根目录
        
    2. 在settings.py 文件加入
    
            MEDIA_ROOT = os.path.join(BASE_DIR, 'static/upload')

    3. HTML文件表单

            <form action="{% url 'image_field' %}" method="post" enctype="multipart/form-data">
            {% csrf_token %}
            <span>请输入用户名：</span><input type="text" name="username" placeholder="请输入用户名">
            <br>
            <span>请上传文件：</span><input type="file" name="image" >
            <br>
            <button name="submit">上传</button>
            </form>

    4. 文件接收函数：

            elif request.method == 'POST':
                username = request.POST.get('username')
                image = request.FILES.get('image')
                user = UserModel()
                user.u_name = username
                user.u_icon = image
                user.save()
                return HttpResponse('上传成功')
                
4. 静态文件获取：

        def mine(request):
            username = request.GET.get('username')
            user = UserModel.objects.get(u_name=username)
            print('/static/upload/' + user.u_icon.url)    # 拼接了settings 里MEDIA_ROOT路径
            context = {
                'username': user.u_name,
                'img_url': img_url
            }
            return render(request, 'mine.html', context=context) 
            
    模板渲染：
    <h2>{{ username }}</h2>
    <img src="{{ img_url }}" alt="{{ username }}">

5. 关于上传文件路径：

        class UserModel(models.Model):
        u_name = models.CharField(max_length=16)
        
        # upload_to 相对路径， 相对于的是MEDIA_ROOT, 媒体根目录
        u_icon = models.FileField(upload_to='static')

    其中 upload_to='static' 可以改为 ‘%Y/%m/%d/static' 
    Django实现了对日期格式化的功能，这样文件可以按年月日分类存放，减小Linux 崩溃的风险，也便于查找文件。
    
6. 静态资源：

    使用的时候注意配制资源的位置
    
        STATICFILES_DIRS
    
    使用{% load static %}
    
        {% static '相对路径' %}
        
7.            