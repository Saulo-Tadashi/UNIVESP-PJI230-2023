﻿from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]', 'zotakeartesanato.azurewebsites.net', 'www.zotakeartesanato.azurewebsites.net']
CSRF_TRUSTED_ORIGINS = ['zotakeartesanato.azurewebsites.net']
if 'CODESPACE_NAME' in os.environ:
    CSRF_TRUSTED_ORIGINS = [f'https://{os.getenv("CODESPACE_NAME")}-8000.{os.getenv("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN")}']

# WhiteNoise configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'authentication.apps.AuthenticationConfig',
    'order.apps.OrderConfig'
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

WSGI_APPLICATION = 'Zotake_PI2.wsgi.application'

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
conn_str = os.getenv('AZURE_POSTGRESQL_CONNECTIONSTRING')
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': conn_str_params['dbname'],
        'HOST': conn_str_params['host'],
        'USER': conn_str_params['user'],
        'PASSWORD': conn_str_params['password'],
    }
}

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo' 

USE_I18N = True

USE_TZ = True

DEFAULT_FILE_STORAGE = 'core.azure_storage.AzureMediaStorage'
STATICFILES_STORAGE = 'core.azure_storage.AzureStaticStorage'

AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')

LOGIN_REDIRECT_URL = '/order/lista/'
LOGOUT_REDIRECT_URL = '/home/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'