# 安装需要的包

pip install -r ./requirements.txt

# settings.py 配置文件

## 文档

https://docs.djangoproject.com/en/2.1/ref/settings/

项目名/settings.py

## ALLOWED_HOSTS

```
ALLOWED_HOSTS = ['dev.env','localhost','127.0.0.1']
```
项目的 host 白名单；
一个开发建议是通过配置电脑本地的 hosts 文件。

`127.0.0.1    dev.env`

这样，开发时就可以统一的用 dev.env 这个内部域名，也比较方便。

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
如果自己的 app 用到模型，同样的也是在这里加，直接写 app 名。

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