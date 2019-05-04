### 导出/导入虚拟环境模块包:
> 导出: pip freeze > requirements.txt  
> 导入: pip install -r requirements.txt

### Python虚拟环境:
- 创建python指定版本虚拟环境:如下命令
    - mkmirtualenv "虚拟环境名称"
    - mkvirtualenv --python= E:\Developer_Tools\Python\Python36\python.exe "虚拟环境名称"
- 列出所有的虚拟环境：workon
- 启动/切换虚拟环境：workon "虚拟环境名称"
- 新建虚拟环境：mkvirtualenv "虚拟环境名称"
- 删除虚拟环境：rmvirtualenv "虚拟环境名称"
- 退出(离开)虚拟环境：deactivate

### 使用Python-IDEL[虚拟环境]:
- 1.首先终端进入到虚拟环境
- 2.终端下的虚拟环境中执行命令: python -m idlelib.idle
- 3.退出: quit()

### Shell交互工具[虚拟环境]
- 1.首先终端进入到虚拟环境并安装Ipython工具: pip install Ipython
- 2.终端下的虚拟环境中执行命令: ipython
- 3.退出: quit

******************************************************************************************************************
### Python内置模块与函数:
- import json   # json数据
- import random # 随机数
- from urllib import request    # 网络爬虫
- from http.cookiejar import CookieJar  # 管理cookie
- import re # 正则
- import time   # 时间
- import datatime   # 日期时间
- import os # 文件与目录
- import csv    # csv文件读取与写入
- import threading  # 多线程
- from queue import Queue   # 队列



******************************************************************************************************************
### 第三方安装模块:
- import requests   # 爬虫模块: pip install requests
- from lxml import etree    # 数据提取 pip install lxml
- from bs4 import BeautifulSoup # 数据提取 pip install bs4  或者 pip install beautifulsoup4
- from fake_useragent import UserAgent  # 随机获取User-Agent pip install fake-useragent
- from itsdangerous import TimedJSONWebSignatureSerializer as Serializer    # 数据信息加密 pip install itsdangerous
- import pymysql    # 链接数据库 pip install PyMySQL
- import pymongo    # 链接MongoDB数据库 pip install pymongo
- import redis  # 链接Redis数据库 pip install redis



******************************************************************************************************************
### Django框架内置模块与函数: pip install django
- from django.shortcuts import render   # 返回模版信息
- from django.shortcuts import redirect # 重定向到另一个url
- from django.shortcuts import HttpResponse # 返回一个字符串
- from django.http import HttpResponse  # 返回一个字符串
- from django.conf.urls import url,include  # url地址分配与包含另一个urls.py文件
- from django.core.urlresolvers import reverse  # 反向解析url地址
- from django.core.mail import send_mail    # 发送邮件
- from django.views.generic import View # 类视图
- from django.contrib.auth.models import AbstractUser   # 抽象类
- from django.contrib import admin  # 管理员
- from django.db import models  # 模型类



# Django框架内置命令:
- django-admin startproject projectname             # 创建django工程项目
- python manage.py startapp appname                 # 创建app应用
- python manage.py makemigrations                   # 生成迁移文件
- python manage.py migrate                          # 执行迁移文件
- python manage.py createsuperuser                  # 创建超级管理员用户
- python manage.py flush                            # 清空数据库[yes or no]
- python manage.py dumpdata > mysite_all_data.json  # 导出所有数据
- python manage.py loaddata mysite_all_data.json    # 导入所有数据
- python manage.py dumpdata appname > appname.json  # 导出app应用的数据
- python manage.py loaddata appname.json            # 导入app应用的数据
- python manage.py runserver IP/PORT                # 启动django工程项目
- python manage.py shell                            # 项目环境终端
- python manage.py dbshell                          # 数据库命令行

******************************************************************************************************************
### Flask框架内置模块与函数: pip install flask
> from flask import Flask  
> from flask import render_template # 返回.html模版
> from flask import redirect    # url重定向
> from flask import url_for # url反向路由
> from flask import make_response
> from flask import request
> from flask import session
 

- Flask框架扩展(表单): pip install flask_script
    - from flask_script import Manager 


- Flask框架扩展(表单): pip install flask_wtf
    - from flask_wtf import FlaskForm
    - from wtforms import SubmitField,StringField,PasswordField # 表单字段
    - from wtforms.validators import DataRequired,EqualTo   # 表单验证


- Flask框架扩展(数据库): pip install flask-sqlalchemy
    - from flask_sqlalchemy import SQLAlchemy   # 使用数据库前提
        - pip install flask-mysqldb # 使用mysql数据库


- Flask框架扩展(邮件):
    - from flask_mail import Mail, Message
















