import os
import environ
from pathlib import Path
from datetime import timedelta

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env("SECRET_KEY", default="ewfi83f2ofee3398fh2ofno24f")
DEBUG = env("GPT_DEBUG", cast=bool, default=True)

ALLOWED_HOSTS = ['*']
CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]
LOCAL_APPS = [
    'accounts',
    'gpt_core',
]

THIRD_PARTY_APP = [
    'allauth',
    'corsheaders',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',

    'dj_rest_auth',
    'rest_framework.authtoken',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

INSTALLED_APPS = CORE_APPS + THIRD_PARTY_APP + LOCAL_APPS
SITE_ID = 1

AUTH_USER_MODEL = 'accounts.Accounts'

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'mygpt.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
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

WSGI_APPLICATION = 'mygpt.wsgi.application'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://mygpt-client.vercel.app"
]
CSRF_TRUSTED_ORIGINS = ["https://mygpt.redshop.tech/",
                        "https://www.mygpt.redshop.tech/"]


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env("MYDB_NAME", default="myproject"),
            'USER': env("MY_DB_USER", default="myprojectuser"),
            'PASSWORD': env("MY_DB_PASSWORD", default="password"),
            'HOST': env("MY_DB_HOST", default="127.0.0.1"),
            'PORT': env("MY_DB_PORT", default="5432"),
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env("MYDB_NAME", default="myproject"),
            'USER': env("MY_DB_USER", default="myprojectuser"),
            'PASSWORD': env("MY_DB_PASSWORD", default="password"),
            'HOST': env("MY_DB_HOST", default="127.0.0.1"),
            'PORT': env("MY_DB_PORT", default="5432"),
        },
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

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True,
    'AUTH_HEADER_TYPES': ('Bearer', ),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken', ),
}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
    "JWT_AUTH_HTTPONLY": False,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
