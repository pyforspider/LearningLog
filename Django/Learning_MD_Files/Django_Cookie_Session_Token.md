1. Cookie，Session， Token 之 Cookie:

    特性：存储在客户端，键值对存储，支持过期时间，默认Cookie自动携带，本网站所有Cookie。
    注意： Cookie不能跨域名、网站使用。
    使用： 通过HttpResponse

    设置cookie：

        def set_cookie(request):
            response = HttpResponse('设置cookie')
            response.set_cookie('hobby', 'gaming', max_age=60) #设置为None为永不过期
            return response

    获取cookie：

        def get_cookie(request):
            hobby = request.COOKIES.get('hobby')
            return HttpResponse(hobby)
            
2. Cookie 应用：登录

        def login(request):
            if request.method == 'GET':                  # 先去登录页面填表单，
                return render(request, 'login.html')
            elif request.method == 'POST':
                response = HttpResponse('设置cookie成功')
                username = request.POST.get('user')
                
                # 后POST回来让response对象设置cookie
                response.set_cookie('username', username) 
                
            # 这里return不能重定向，否则如果不返回response则cookie设置失败
            return response 
    
            改进版：HttpResponse --> HttpResponseRedirect(reverse(mine))
        
3. Cookie 注意点：

    Cookie不能存中文，如果要存，需要转码，如Base64   
    
4. Cookie 加盐：

        response.set_signed_cookie('content', username, 'rock')
        response.set_signed_cookie('content', username, salt='rock')都可以

        效果如下：
        Welcome, Sunck:1htrNZ:RUmGZaxowVwWgun2IQUgVanO-cs

        去盐：
        username = request.get_signed_cookie('content', salt='rock') #关键字参数salt必须加上
        
5. Cookie 之 删除：

        username = request.get_signed_cookie('content', 'rock')

    由于cookie是由服务端进行操作的，如response.set_cookie()，因此有response.delete_cookie()    

6. Cookie 之 坑点：

    获取cookie时：
    
        username = request.get_signed_cookie('content', salt='rock') 
        必须指定关键字salt，否则获取的就一直是rock (原因未知，需查看源码)
        
7. Session 会话技术：

    数据存储在服务器，默认Session存储在内存中，Django中默认会把session持久化到数据库中。
    表名 django_session
    属性 session_key , session_data, expire_date(过期时间)

    往数据库存session的操作：
    
        request.session['user'] = user # 右边的变量user 由表单提交的POST而来，可以在表单中存中文，使用Base64编码

    存在客户端Cookie(因此依赖Cookie)的sessionid 和 服务器数据库端的session_key的值一样，默认有效期为2个星期。
    获取session的操作：
    
        user = request.session.get('user') 

8. Session 之 删除：

    方法 ： 
        1、删除Cookie中的sessionid (没有连字符) 
        2、删除session_key 
        3、删除Cookie和session_key

        1、 response.delete_cookie('sessionid') # 缺点：数据库里没删，产生垃圾数据
        
        2、 del request.session['user'] # 如果redirect到mine主页时，第一次正常退出，显示None，点击第二次退出时，由于数据库没有user不完整，会报错。正常来讲应该redirect到login界面。 缺点：浏览器缓冲sessionid没删
        
        3、 request.session.flush() # 此种方法删除最完全
        
9. Session 设置、获取、删除：

        requset.session['user'] = user # 设置 session
        
        request.session.get['user'] # 获取user的值
        
        session.session_key # 获取session的key

    以下删除方法：

        session.clear() # 方法清空当前所有会话
        session.flush() # 删除当前会话数据，清除sessionid ###最优
        del requset.session['user'] # 删除session会话，但数据库的删除不完全
        response.delete_cookie('sessionid') # 删除客户端Cookie中sessionid
        
10. Token 服务端会话技术：

    1、自定义的session
    
    2、兼容不支持cookie的终端，如移动端 则使用 JsonResponse , 移动端进入 mine页面时，需要在 url中穿递 token， 如 http://127.0.0.1:8000/two/usermine/?token=325
    
    3、如果在web开发中，使用和session基本一致
    
    4、如果使用在移动端或者客户端开发中，通常以json形式传输，获取 token 关联的数据时，主动传递 token           
    
11. Token 设置：

    1、创建数据库表，设置u_token 字段 
    
    2、在用户注册完，再次进行登录时，使用hash生成一个随机token，并response设置到用户的Cookie中去
    
    3、当用户想要进入mine页面，则将cookie中的 token字段取出，检索出服务器数据库端的 有此 token 用户，并展示相关页面
    
    4、至于退出登录，应该是清空 数据库的token字段 
    
12. Cookie 和 Session、Token比较

    1、Cookie使用更简洁，服务器压力更小，数据不是很安全
    
    2、Session 服务器要维护session，相对安全
    
    3、Token 拥有Session所有优点，维护略麻烦， 但支持更多终端                          