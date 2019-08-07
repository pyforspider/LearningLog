1. 用途介绍

    * 实现统计功能：
    统计IP，统计浏览器
    
    * 实现权重控制：
    黑名单，白名单
    
    * 实现反爬：
    反爬虫(10s之内只能搜索一次)， 频率控制
    
    * 界面友好化，应用交互友好化

2. 切入函数：切点

    1. __init__
    
    2. process_request(self, request)
    
    3. process_view(self, request, view_func, view_args, view_kwargs)
    
    4. process_template_response(self, request, response)
    
    5. process_response(self, request, response)
    
    6. process_exception(self, request, exception)

    中间件调用顺序：
    按列表依次执行，如果有返回，则后续中间件不再执行
    
3. 自定义中间件流程：

    1. 在工程目录下创建midddleware目录
    
    2. 目录中创建python文件    
    
    3. 在python文件中导入中间件的基类
    
            from django.utils.deprecation import MiddlewareMixin
    
    4. 在类中根据功能需求， 创建切入需求类， 重写切入点方法
    
            class LearnAOP(MiddlewareMixin):
                def process_request(self, request):
                    print('request路径', request.path)
    
    5. 启用中间件， 在settings里进行配置， MIDDLEWARE中添加middleware.文件名.类名

4. 切点 process_request(self, request)

    在执行视图函数前被调用， 每个请求上都会调用， 不主动进行返回或返回HttpResponse对象。

        class LearnAOP(MiddlewareMixin):
            def process_request(self, request):
                ip = request.META.get('REMOTE_ADDR')
                print('请求的IP地址：', path, request.path)
    
                if request.path == '/app/getphone/':
                    if ip == '127.0.0.1':
                        if random.randrange(0, 100) > 10:
                        return HttpResponse('VIP，恭喜你抢到手机了')

                if request.path == '/app/getticket/':
                    if ip.startswith('10.0.127.7'):
                        return HttpResponse('黑名单抢卷失败')

                if request.path == '/app/search/': # 一定要注意注意地址斜杠相匹配
                    result = cache.get(ip)
                    if result:
                        return HttpResponse('请求过于频繁')
                    cache.set(ip, ip, timeout=3)
                        
5. 限制60s内访问次数不超过10：

    在process_request内加上以下代码：需提供变量ip

        requests = cache.get(ip, [])
        if requests and time.time() - requests[-1] > 60:        # 弹出列表中 超过60s 的时间戳
            requests.pop()
        if len(requests) > 10:                                  # 列表时间戳数量大于10 时
            return HttpResponse('请求过于频繁，小爬虫回家睡觉吧')
        requests.insert(0, time.time())                         # 在列表最前索引位置 插入时间戳
        cache.set(ip, requests)                                 # 当前缓存插入列表 
        
6. 限制恶意ip访问：

    在process_request函数中加入：提供ip

        black_list = cache.get('black', [])
        if ip in black_list:
            return HttpResponse('对不起，你已在黑名单中，禁止访问本网站')

        requests = cache.get(ip, [])
        if requests and time.time() - requests[-1] > 60:             # 弹出列表中 超过60s 的时间戳
            requests.pop()
        requests.insert(0, time.time())                              # 列表插入时间戳 insert(index, content)
        cache.set(ip, requests)                                      # 当前缓存插入列表

        if len(requests) > 30:                                       # 列表时间戳数量大于30 时
            black_list.append(ip)
            cache.set('black', black_list, timeout=60*60*24)
            return HttpResponse('请求过于频繁，黑名单见')
            
7. 处理服务器错误500：

    假设视图函数里有：

        def calc(request):
            a, b = 10, 20
            c = (a+b)/0
            return HttpResponse(c)

    则在中间件里加入：

        def process_exception(self, request, exception):
            return redirect(reverse('get_xm'))
            
8. form表单没有添加{% csrf_token %}，可以通过添加豁免权，豁免csrf验证：

        @csrf_exempt
        def login(request):
            if request.method == 'GET':
                return render(request, 'login.html')
            elif request.method == 'POST':
                return HttpResponse('POST登录成功')

9. 