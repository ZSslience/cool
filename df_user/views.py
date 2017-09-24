from django.shortcuts import render,redirect
from django.http import HttpResponseNotAllowed
from django.views.decorators.http import require_POST,require_GET,require_http_methods
from df_user.models import Passport
# Create your views here.
# http://127.0.0.1:8000/user/register/
'''
def require_POST(view_func):
    def wrapper(request, *args, **kwargs):
        if request.method != 'POST':
            return HttpResponseNotAllowed('not allowed')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper
'''

@require_http_methods(['GET','POST'])
def register(request):
    '''
    显示注册页面
    '''
    if request.method == 'GET':
        # 显示注册页面
        return render(request, 'register.html')
    elif request.method == 'POST':
        # 进行用户注册处理
        # 1.接收用户的注册信息
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        # 2.将用户的注册信息保存进数据库
        '''
        passport = Passport()
        passport.username = username
        passport.password = password
        passport.email = email
        passport.save()
        '''
        Passport.objects.add_one_passport(username=username, password=password, email=email)
        # 3.跳转到登录页面
        return redirect('/')


@require_POST
def register_handle(request):
    '''
    用户注册处理
    '''
    # 1.接收用户的注册信息
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    # 2.将用户的注册信息保存进数据库
    passport = Passport()
    passport.username = username
    passport.password = password
    passport.email = email
    passport.save()
    # 3.跳转到登录页面
    return redirect('/')
