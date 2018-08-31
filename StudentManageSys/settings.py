from __future__ import absolute_import, unicode_literals
import os

# Celery settings

CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'
CELERY_TASK_SERIALIZER = 'json'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%!tk$*mhe*8ox(w3l_6a#%oo-8(0onzobuzrzw5^!aos)r=e)y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    # 'django_celery_results',
    'rest_framework',
    'authentication',
    'user_info',
    'campus',
    'channel',
    'coupon',
    'course',
    'order',
    'project',
    'student',
    'log_info',
    'payment',
    'record',
    'student_course',
    'complain',
    'message',
    'common',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'middleware.auth_middle.AuthMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
)

ROOT_URLCONF = 'StudentManageSys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15,
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend', 'rest_framework.filters.SearchFilter'),
    'DEFAULT_RENDERER_CLASSES': (
        'utils.renderers.CustomJsonRender',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'EXCEPTION_HANDLER': 'utils.handlers.exception_handler'
}

WSGI_APPLICATION = 'StudentManageSys.wsgi.application'

LOG_ROOT = os.path.join(BASE_DIR, 'logs')
if not os.path.isdir(LOG_ROOT):
    os.makedirs(LOG_ROOT)

# 日志系统
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '%s/log.log' % LOG_ROOT,
            'formatter': 'simple'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.db': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        }
    }
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student_manage_sys',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': 3306,
        'CHARSET': 'UTF-8',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 系统启动默认创建media文件夹
if not os.path.exists(MEDIA_ROOT):
    os.mkdir(MEDIA_ROOT)
# 系统启动默认创建media/channel文件夹存放渠道二维码
if not os.path.exists(os.path.join(MEDIA_ROOT, 'channel')):
    os.mkdir(os.path.join(MEDIA_ROOT, 'channel'))
# 系统启动默认创建media/agreement文件夹存放学生电子协议图片
if not os.path.exists(os.path.join(MEDIA_ROOT, 'agreement')):
    os.mkdir(os.path.join(MEDIA_ROOT, 'agreement'))
# 系统启动默认创建media/transcript文件夹存放学生成绩单
if not os.path.exists(os.path.join(MEDIA_ROOT, 'transcript')):
    os.mkdir(os.path.join(MEDIA_ROOT, 'transcript'))
# 系统启动默认创建media/IDcard1文件夹存放学生身份证图片
if not os.path.exists(os.path.join(MEDIA_ROOT, 'IDcard1')):
    os.mkdir(os.path.join(MEDIA_ROOT, 'IDcard1'))
# 系统启动默认创建media/IDcard2文件夹存放学生身份证图片
if not os.path.exists(os.path.join(MEDIA_ROOT, 'IDcard2')):
    os.mkdir(os.path.join(MEDIA_ROOT, 'IDcard2'))
# 系统启动默认创建media/IDcard1文件夹存放学生订单支付信息图片
if not os.path.exists(os.path.join(MEDIA_ROOT, 'order')):
    os.mkdir(os.path.join(MEDIA_ROOT, 'order'))
# 系统启动默认创建media/images/user_qrcode文件夹存放系统用户二维码
if not os.path.exists(os.path.join(MEDIA_ROOT, 'images/user_qrcode')):
    os.makedirs(os.path.join(MEDIA_ROOT, 'images/user_qrcode'))
# 系统启动默认创建media/images/certificate文件夹存放系统审课图片
if not os.path.exists(os.path.join(MEDIA_ROOT, 'images/certificate')):
    os.makedirs(os.path.join(MEDIA_ROOT, 'images/certificate'))
# 系统启动默认创建media/images/convert文件夹存放系统审课图片
if not os.path.exists(os.path.join(MEDIA_ROOT, 'images/convert')):
    os.makedirs(os.path.join(MEDIA_ROOT, 'images/convert'))
# 系统启动默认创建media/images/complain文件夹存放用户投诉图片
if not os.path.exists(os.path.join(MEDIA_ROOT, 'images/complain')):
    os.makedirs(os.path.join(MEDIA_ROOT, 'images/complain'))

# redis 配置
REDIS_CONFIG = {
    'host': 'localhost',
    'port': 6379
}
# elastic-search 配置
ELASTIC_SEARCH_CONFIG = {
    'host': '47.105.104.233',
    'port': 9200
}

# 生成token需要的秘钥
SECURE_KEY = {
    'SECRET_KEY': '785CHINASUMMER85ISWONDERFUL89HAHA42',
    'AUTH_SALT': 'A1FE3FGE4RW5G9'
}

# 配置不需要认证的后端url
ignore_auth_urls = ['/api/v1/student/info/authorize', '/api/v1/user_info/login/']

# 服务器域名
DOMAIN = 'http://student_test.lxhelper.com'

MEDIA_URL = '/media/'

# 公众号消息推送模板编号
template_info = {
    'match_success': 'YeMDfDi25UrcAWLV4GKT2YV3ihrV6LxZH_EZwVxWAVo',
    'invite_success': '5QiQJNjdkcOSSPgx5W4A0xEBXTuITRwT62YcdOro_iU',
    'attend_result_notice': 'px45KahMC3zCEXe78el4-tHBYQtBFrtwvwQY3JW0xw8'
}

# 微信公众号配置
WX_CONFIG = {
    'APP_ID': 'wx622bf44e0bee4f2b',
    'APP_SECRET': '97d4204adeb370336439e67bab275155'
}

# Django 邮件服务器配置

# 这一项是固定的
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# smtp服务的邮箱服务器 我用的是163
EMAIL_HOST = 'smtp.qq.com'
# smtp服务固定的端口是25
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = '52100141@qq.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'kfznegjwtjfhbjbj'
# 收件人看到的发件人 <此处要和发送邮件的邮箱相同>
EMAIL_FROM = 'python<52100141@qq.com>'
