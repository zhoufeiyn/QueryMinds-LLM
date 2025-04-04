"""
Django settings for sqltasks project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_h%%#i87n!ew4*x@t+0(0z#=e^37#+5u7(78ug&zv)=-k$i8^5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'llminteract',  # 添加llminteract应用

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',  # 添加whitenoise中间件
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sqltasks.urls'

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

WSGI_APPLICATION = 'sqltasks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
import pymysql # noqa: 402
import os
pymysql.version_info = (1, 4, 6, 'final', 0) # change mysqlclient version
pymysql.install_as_MySQLdb()
DATABASES = {
       'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'neu_db_project',
        'USER': 'neu-db-user',
        'PASSWORD': 'PhT<\[*673._c7V+',
        'HOST': '34.169.163.169',
        'PORT': '3306',
    }
}

# import pymysql # noqa: 402
# import os
# pymysql.version_info = (1, 4, 6, 'final', 0) # change mysqlclient version
# pymysql.install_as_MySQLdb()
# if os.getenv('GAE_APPLICATION', None):
#     DATABASES = {
#         'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': '/cloudsql/db-002080320:us-west1:neu-test-db',
#         'USER': 'root',
#         'PASSWORD': 'Zfy,199512',
#         'NAME': 'lab10',}
#         }
# else:
#     DATABASES={
#         'default':{
#             'ENGINE':'django.db.backends.mysql',#连接mysql
#             'NAME':'lab10', #数据库名字
#             'USER':'root',
#             'PASSWORD': 'Zfy,199512',
#             'HOST':'35.230.58.209',
#             'PORT':3306,
#         }
#     }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = 'static'
STATIC_URL = '/static/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# WHITENOISE_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#
# # 配置WhiteNoise
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#
# # 配置会话
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# SESSION_COOKIE_AGE = 86400  # 会话有效期为1天
#
# # 安全设置
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = False
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')