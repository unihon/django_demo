# 安装需要的包

pip install -r ./requirements.txt

# settings.py 配置文件

## 文档

https://docs.djangoproject.com/en/2.1/ref/settings/

项目名/settings.py

## ALLOWED_HOSTS

```
ALLOWED_HOSTS = ['localhost','127.0.0.1']
```

项目的 host 白名单

## INSTALLED_APPS

```
INSTALLED_APPS = [
        # 'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        ]
```

不用 admin apps，添加 rest_framework；  
如果自己的 app 用到模型，同样的也是在这里加，直接写 app 名

## DRF

```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}
```

开发时用到的两个渲染器。

# VSCode 的 debug 配置

```
"configurations": [
    {
        "name": "Python: Django",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}/manage.py",
        "args": [
            "runserver",
            // "--noreload",
            "0:8000"
        ],
        "django": true,
        "console": "integratedTerminal"
    }
]
```

# 基本流程

``` python
# 创建 app
python manage.py startapp appname

# 给 app 添加一个 urls.py
# 在项目目录的 urls.py 中引入 app 的 urls.py

from django.urls import include, path
urlpatterns = [
        path('apppath', include('appname.urls')),

# 编写 app 的 urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('', views.Apple.as_view()),
    path('object', views.Sydney.as_view()),

]

# 其中 views.XX，的 XX 是 app views.py 中的类

``` 
