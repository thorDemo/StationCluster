"""
Django settings for StationCluster project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ulb+pe%d6^s4mdp3yb%&l30judz4(&@(6b9idq*(uu&o2_976x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'CPModel_1.apps.CPModel1Config',
    'CPModel_2.apps.CPModel2Config',
    'CPModel_3.apps.CPModel3Config',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'sorl.thumbnail',
]

MIDDLEWARE = [
    # 'django_hosts.middleware.HostsRequestMiddleware',
    'Middleware.DomainMiddleware.MultipleDomainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#
# MULTIPLE_UFL_CONFIG = {
#     'www.bjgirls.cn': 'StationCluster.urls_1',
#     'www.bjdirectory.cn': 'StationCluster.urls_2',
#     'www.bjflowers.cn': 'StationCluster.urls_2',
#     'www.example1.com': 'StationCluster.urls_2',
#     'www.example2.com': 'StationCluster.urls_2',
# }

ROOT_URLCONF = 'StationCluster.urls_1'
# ROOT_HOSTCONF = 'StationCluster.hosts'
DEFAULT_HOST = 'api'

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


WSGI_APPLICATION = 'StationCluster.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'station',
        'USER': 'station',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3339',
    }
}
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'station',
#         'USER': 'root',
#         'PASSWORD': '123456',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, '/static/')


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "CPModel_1/templates/CPModel_1/static"),
    os.path.join(BASE_DIR, "CPModel_2/templates/CPModel_2/static"),
    os.path.join(BASE_DIR, "CPModel_2/templates/CPModel_2/static/img"),
    os.path.join(BASE_DIR, "CPModel_3/templates/CPModel_3/static"),
)

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (50, 50), 'crop': True},
    },
}