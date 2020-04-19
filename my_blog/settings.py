import os,sys,platform

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '__=s9@oixaun$x^g7-4#10wf_*7zvb8)kl1$j82fj&cyq%^o^3'

# Application definition
INSTALLED_APPS = [
    'xadmin',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 可添加需要的第三方登录
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.weibo',

    'password_reset',
    'taggit',
    'ckeditor',
    'ckeditor_uploader',
    'mptt',
    'notifications',

    'article',
    'userprofile',
    'comment',
    'notice',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 定义模板位置
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

ALLOWED_HOSTS = ['*']
STATIC_URL = '/static/'
# 媒体文件地址
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
CKEDITOR_UPLOAD_PATH = 'upload/'
CKEDITOR_IMAGE_BACKEND = 'pillow'

if "Windows" in platform.platform():
    DEBUG = True
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # 'django.db.backends.sqlite3',
            'HOST': '127.0.0.1',  # 'NAME': os.path.join(BASE_DIR, 'db.mysq')#'db.sqlite3'),
            'PORT': '3306',
            'NAME': 'dsdjango',
            'USER': 'qq1788lover',
            'PASSWORD': 'qq1010351486',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4'
            },
        }
    }
if "Linux" in platform.platform():
    DEBUG = True
    STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')  # 静态文件收集目录
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # 'django.db.backends.sqlite3',
            'HOST': '127.0.0.1',  # 'NAME': os.path.join(BASE_DIR, 'db.mysq')#'db.sqlite3'),
            'PORT': '3306',
            'NAME': 'dsdjango',
            'USER': 'root',
            'PASSWORD': 'qq1788lover',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4'
            },
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'#'en-us'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# SMTP服务器
EMAIL_HOST = 'your smtp'
# 邮箱名
EMAIL_HOST_USER = 'your email'
# 邮箱密码
EMAIL_HOST_PASSWORD = 'your password'
# 发送邮件的端口
EMAIL_PORT = 25
# 是否使用 TLS
EMAIL_USE_TLS = True
# 默认的发件人
DEFAULT_FROM_EMAIL = 'your email'


# CKEDITOR_CONFIGS = {
#     # django-ckeditor默认使用default配置
#     'default': {
#         # 编辑器宽度自适应
#         'width':'auto',
#         'height':'250px',
#         # tab键转换空格数
#         'tabSpaces': 4,
#         # 工具栏风格
#         'toolbar': 'Custom',
#         # 工具栏按钮
#         'toolbar_Custom': [
#             # 表情 代码块
#             ['Smiley', 'CodeSnippet'],
#             # 字体风格
#             ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
#             # 字体颜色
#             ['TextColor', 'BGColor'],
#             # 链接
#             ['Link', 'Unlink'],
#             # 列表
#             ['NumberedList', 'BulletedList'],
#             # 最大化
#             ['Maximize']
#         ],
#         # 插件
#         'extraPlugins': ','.join(['codesnippet', 'prism', 'widget', 'lineutils']),
#     }
# }

CKEDITOR_CONFIGS = {
    'default': {
        'update': ['Image', 'Update', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
        'skin': 'moono',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms','items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton','HiddenField']},
            '/',
            {'name': 'basicstyles','items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph','items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert','items': ['Image',
                                        # 'Flash',
                                        'Table', 'HorizontalRule', 'Smiley','CodeSnippet','SpecialChar', 'PageBreak', 'Iframe']},
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'yourcustomtools', 'items': ['Preview','Maximize',]},  # 自定义控件
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                # your extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
                'codesnippet',
                'prism',
            ]),
    }
}



AUTHENTICATION_BACKENDS = (
    # 此项使 Django 后台可独立于 allauth 登录
    'django.contrib.auth.backends.ModelBackend',
    # 配置 allauth 独有的认证方法，如 email 登录
    'allauth.account.auth_backends.AuthenticationBackend',
)

# 设置站点
SITE_ID = 1
# 重定向 url
LOGIN_REDIRECT_URL = '/'

# LOGGING = {
#     'version': 1,
#     'handlers': {
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'INFO',
#         },
#     },
# }

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter': 'verbose',
#         },
#         'file': {
#             'level': 'WARNING',
#             # 'class': 'logging.FileHandler',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'when': 'midnight',
#             'backupCount': 30,
#             'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
#             'formatter': 'verbose',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['file', 'mail_admins'],
#             'level': 'WARNING',
#             'propagate': False,
#         },
#     }
# }