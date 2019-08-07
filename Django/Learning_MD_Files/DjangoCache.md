1. 简介：
    * 为了提升服务器的响应速度
    * 对于已访问过的资源进行下载，再次访问时直接使用缓存
    * 内存级缓存最为适用
    * Django内置缓存框架
    
2. 使用：

    1. 创建数据库表
    
            python manage.py createcachetable [table_name]

    2. settings.py 中进行缓存配置：
    
            CACHES = {
                'default': {
                    'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
                    'LOCATION': 'my_cache_table',
                    'TIMEOUT': 60 * 5,
                }
            }

    3. 使用

            def news(request):
                news_list = []
                for i in range(10):
                    news_list.append('最近贸易战又开始了%s' % i)
                sleep(5)
                data = {
                    'news_list': news_list,
                }
                return render(request, 'news.html', context=data)
	
        加上装饰器 @cache_page(timeout) 即可实现页面缓存。timeout为缓存失效时间。
        
3. 不使用装饰器 @cache_page()

        def news(request):
            result = cache.get('news')
                if request:
                    return HttpResponse(result)
            news_list = []
            for i in range(10):
                news_list.append('最近贸易战又开始了%s' % i)
            sleep(5)
            data = {
            'news_list': news_list,
            }
            response = render(request, 'news.html', context=data)
            cache.set('news', response.content, timeout=30) 		#设置缓存
            return response
            
4. 使用装饰器：

        @cache_page(60, cache='default')
        def jokes(request):
            sleep(5)
            return HttpResponse(‘joke_list’)
            
5. redis 实现快速缓存：

    1. 两个包 pip install

            django-redis
            django-redis-cache

    2. settings设置：

            CACHES = {
                "default": {
                    "BACKEND": "django_redis.cache.RedisCache",
                    "LOCATION": "redis://127.0.0.1:6379/1",
                    "OPTIONS": {
                        "CLIENT_CLASS": "django_redis.client.DefaultClient",
                    }
                }
            }

    3. 刷新网页（之前没有用装饰器的视图函数）

    使用命令台查看数据：

        redis-cli
        select 1
        keys *                  # 查看当前存在的值， 返回“:1:news”
        get :1:news #返回结果
        ttl :1:news #查看有效时间 
        
6. Django可以实现多方式缓存：

    1. settings.py文件：

            CACHES = {
                'default': {
                    'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
                    'LOCATION': 'my_cache_table',
                    'TIMEOUT': '60',
                },
            
                "redis_backend": {
                    "BACKEND": "django_redis.cache.RedisCache",
                    "LOCATION": "redis://127.0.0.1:6379/1",
                    "OPTIONS": {
                        "CLIENT_CLASS": "django_redis.client.DefaultClient",
                    }
                }
            }

    2. 注释之前的 cache 模块，导入 from django.core.cache import caches 模块
    在函数添加 cache = caches['redis_backend'], 即完成

            def news(request):
                cache = caches['redis_backend']
                result = cache.get('news')
                if result:
                    return HttpResponse(result)
                sleep(5)
                response = HttpResponse('测试缓存成功，以保存缓存')
                cache.set('news', response.content, timeout=30)
                return response

    使用装饰器：

        @cache_page(60, cache='default')
        def jokes(request):
            sleep(5)
        return HttpResponse(‘joke_list’)  
        
7. 使用：

        cache.get(key)
        
        cache.set(key, value, timeout=int)
    
    例如：
    
        cache.get('news')
        
        cache.set('news', 'content', timeout=60)                                     