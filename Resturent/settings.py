
"""
Django settings for Resturent project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import whitenoise
from django.utils.translation import ugettext_lazy as _
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
temp_dir= os.path.join(BASE_DIR,'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&1g!-ud1gyduc(d^^p2fhj-m2uizx!w*p0+3#rlfurd&cr(o*m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
   ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['185.201.9.176','myfrenchfactorylangkawi.com','127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Main',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Resturent.urls'
# Provide a lists of languages which your site supports.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [
            temp_dir,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Resturent.wsgi.application'

# email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # During deployment only
EMAIL_HOST = 'smtp.mail.yahoo.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'myfrenchfactory@yahoo.com.my'
EMAIL_HOST_PASSWORD = 'ndlfdpekybsrkpjh'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'My French Factory Team <noreply@example.com>'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

#if DEBUG:
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}
#else:
 #   DATABASES = {
  #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
   #     'NAME': 'mffdb',
    #    'USER': 'mffadmin',
     #  'HOST': 'localhost',
      #  'PORT': '',
       # }
    #}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'fr'

# ugettext = lambda s: s
LANGUAGES = (
    ('en-us', _('English')),
    ('fr', _('French')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Set the default language for your site.
# Tell Django where the project's translation files should be.
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/statics/'
# VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT= os.path.join(BASE_DIR,"staticfiles")
# STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,"static")
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')