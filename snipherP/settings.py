"""
Django settings for snipherP project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#mp)ha0kg%#g$=kdkbl95kggp611d#(7d6*fk3q^r$1%2xx885'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'portifolio.apps.PortifolioConfig',
    'newsletters',
    'cloudinary_storage',
    'cloudinary',

    'ckeditor',
    'ckeditor_uploader',
    'django_filters',
    'crispy_forms',
    'storages',
    'social_django',
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

ROOT_URLCONF = 'snipherP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'snipherP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    #{
        #'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #},
    #{
        #'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #},
    #{
        #'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    #{
        #'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #},
]

AUTHENTICATION_BACKENDS = (

    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '318608959945983'
SOCIAL_AUTH_FACEBOOK_SECRET = '5da1de9a3f703e4ae214ac896518763d'

SOCIAL_AUTH_GITHUB_KEY = '6370f7cff9a2d74e91d3'
SOCIAL_AUTH_GITHUB_SECRET = '544117b8ddfef4669489f9e15a0bc75a34bc9f3d'

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '77vuwweasf3kmn'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'cwWo7ahJtYPjYUzp'

SOCIAL_AUTH_TWITTER_OAUTH1_KEY = 'T5VKlPT1SGbool86tJS4Ld6jT'
SOCIAL_AUTH_TWITTER_OAUTH1_SECRET = 'RvwUTs0ONxnsCAgZLnv0jqbSI4TojbSmueiXhkTxTGbIPZkIEl'
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "snipherblog@gmail.com"
EMAIL_HOST_PASSWORD = 'jydqhivfgiamdcjs'


CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'snipher',
    'API_KEY': '421162441822348',
    'API_SECRET': 'gpP7UebOBTHV99kXyBfPDtW2fmk'
}



DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

FROM_EMAIL = 'snipherdev@gmail.com'
SENDGRID_API_KEY = os.environ.get('SENDI_GRID_API_key')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
