from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = 'django-insecure-iu@$(vy3uv_u4g=#r*#ur6^o%#o&lu3fzjh@%l%)#(w9v8x#jx'
SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False if 'WEBSITE_HOSTNAME' in os.environ else True

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

if 'CODESPACE_NAME' in os.environ:
    CSRF_TRUSTED_ORIGINS = [f'https://{os.getenv("CODESPACE_NAME")}-8000.{os.getenv("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN")}']

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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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

# POSTGRESQL local
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME': os.environ.get('DBNAME'),
		'USER' : os.environ.get('DBUSER'),
		'PASSWORD' : os.environ.get('DBPASS'),
		'HOST' : os.environ.get('DBHOST'),
        'PORT': os.environ.get('DBPORT'),
    }
}

#SQLITE - teste na mem�ria RAM
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}'''

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

LANGUAGE_CODE = 'pt-br' #idioma portugues/BR

TIME_ZONE = 'America/Sao_Paulo' #zona de Sao Paulo

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'static'), #pasta static na raiz para organiza��o

)

# Arquivos enviados pelos usu�rios
MEDIA_URL = 'upload/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'upload') #pasta upload na raiz para organiza��o

# Redireciona para a URL da p�gina principal ap�s login
LOGIN_REDIRECT_URL = '/order/lista/'
LOGOUT_REDIRECT_URL = '/home/'

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
