# -*- coding:utf-8 -*-
# @Desc : django项目中间件
# @Author : Administrator
# @Date : 2019-06-04 15:10

# Django项目中settings.py中默认的middleware中间件:
'''
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
'''

### 自定义中间件,中间件在全局操作Django项目的请求与响应
from django.utils.deprecation import MiddlewareMixin

# 1. 定义一个类,可以定义五个方法,常用有process_request和process_response方法
class MyMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        执行顺序: 按照settings.py文件的中间件注册顺序,从上到下
        何时执行: 请求从wsgi拿到的时候
        返回值: None或HttpResponse对象
            如果是None,继续执行后续的中间件的process_request方法
            如果是HttpResponse对象,不执行后续的中间件的process_request方法
        """
        pass

    def process_response(self, request, response):
        """
        执行顺序: 按照settings.py文件的中间件注册顺序,从下到上
        何时执行: 请求有响应的时候
        返回值: 必须是HttpResponse对象
        """
        pass

    # def process_view(self, request, callback, callback_args, callback_kwargs):
    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        :param request: 浏览器发来的请求对象
        :param view_func: 将要执行的视图函数的名字
        :param view_args: 位置参数
        :param view_kwargs: 关键字参数
        执行顺序: 按照settings.py文件的中间件注册顺序,从上到下
        何时执行: 在urls.py中找到与视图的对应关系后,在执行真正的视图函数之前调用
        返回值:
            如果是None,继续执行后续的中间件的process_view方法
            如果是HttpResponse对象,不执行后续的中间件的process_view方法
        """
        pass

    # process_exception方法只有在视图函数中出现异常才执行
    def process_exception(self, request, exception):
        """
        执行顺序: 按照settings.py文件的中间件注册顺序,从下到上
        何时执行: 在视图函数中抛出异常时执行
        返回值:
            如果是None,继续执行后续中间件的process_exception方法
            如果是HttpResponse对象,不执行后续中间件的process_exception方法
        """
        pass

    def process_template_response(self, request, response):
        """
        执行顺序: 按照settings.py文件的中间件注册顺序,从下到上
        何时执行: 在视图函数完成后执行,前提是:视图函数返回的对象有一个render()方法(或表明该对象是一个TemplateResponse对象或等价方法)
        返回值:
            如果是None,继续执行后续中间件的process_exception方法
            如果是HttpResponse对象,不执行后续中间件的process_exception方法
        """
        pass

# 注: 这五个方法的返回值可以是None或HttpResponse对象:
    # 如果是None,则按照Django定义的规则往下执行
    # 如果是HttpResponse对象,则直接将该对象返回给用户
# 注: Django调用 注册的中间件里面的五个方法的执行顺序:
    # process_request  ---> urls.py ---> process_view ---> view.py ---> process_exception ---> process_template_response ---> process_response

# 2. 在seetings.py文件的中添加自定义的中间件
'''
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middlewaredemo.MyMiddleware',  # 自定义中间件
]
注: 中间件有从上到下的执行顺序
'''



