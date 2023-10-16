"""
Django settings for Zotake_PI2 project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iu@$(vy3uv_u4g=#r*#ur6^o%#o&lu3fzjh@%l%)#(w9v8x#jx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig'
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

ROOT_URLCONF = 'Zotake_PI2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], #inclus�o do caminho dos templates
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

TEMPLATE_DIRS = (

    os.path.join(BASE_DIR, 'templates'), #pasta templates na raiz para organiza��o

)

WSGI_APPLICATION = 'Zotake_PI2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'db_zotake'),
		'USER' : 'postgres',
		'PASSWORD' : '123456',
		'HOST' : 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-BR' #idioma portugu�s/BR

TIME_ZONE = 'America/Sao_Paulo' #zona de S�o Paulo

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'static'), #pasta static na raiz para organiza��o

)

# Arquivos enviados pelos usu�rios
MEDIA_URL = 'upload/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'upload') #pasta upload na raiz para organiza��o

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {

    'version': 1,

    'disable_existing_loggers': False,

    'formatters': {

        'simple': {

            'format': 'Mensagem: %(levelname)s %(message)s'

        },

    },

    'handlers': {

        'console': {

            'level': 'DEBUG',

            'class': 'logging.StreamHandler',

            'formatter': 'simple'

        },

    },

    'loggers': {

        'Zotake_PI2': {

            'handlers': ['console'],

            'level': 'DEBUG',

            'propagate': True,

        },

        'main': {

            'handlers': ['console'],

            'level': 'DEBUG',

            'propagate': True,

        },

    },

}
