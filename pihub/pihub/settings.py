import django.conf.global_settings as defaults
import os
import sys

PROJECT_DIR = os.path.join(os.path.dirname(__file__), '../../')

ADMINS = (
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = []

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

MIDDLEWARE_CLASSES = defaults.MIDDLEWARE_CLASSES

ROOT_URLCONF = 'pihub.urls'

TEMPLATE_CONTEXT_PROCESSORS = defaults.TEMPLATE_CONTEXT_PROCESSORS


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pihub.wsgi.application'

TEMPLATE_DIRS = ()


PROJECT_APPS = [
    'pypackages',
    ]

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.github.GithubBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

INSTALLED_APPS = [
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.sites',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                     'django.contrib.admin',

                     'south',
                     'social_auth',
                     'gunicorn',

                     ] + PROJECT_APPS

#AUTH_PROFILE_MODULE = 'account.UserProfile'
#LOGIN_REDIRECT_URL = '/account/profile/edit'
#LOGIN_URL = '/user/login'


SERVE_MEDIA=False


# Default caching config is to simply do nothing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
}



# Celery configuration
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_IMPORTS = (
)
CELERY_LOG_LEVEL = 'INFO'



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        'simple': {
            'format': '%(levelname)s %(message)s'
            },
        },

    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level': 'DEBUG',
            'class':'django.utils.log.NullHandler',
            },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        },

    'loggers': {
        'django.db.backends': {
            'handlers': ['null'],  # Quiet by default!
            'propagate': False,
            'level':'DEBUG',
            },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

MEDIA_URL = '/media/'
STATIC_URL = '/media/static/'


# The rest of the settings come from the environment
if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY']
else:
    sys.stderr.write("The required environment variable SECRET_KEY was not set")
    sys.exit(1)

import dj_database_url
if 'DATABASE_URL' in os.environ:
    DATABASE_URL = os.environ['DATABASE_URL']
    if DATABASE_URL == 'sqlite://:memory:':
        # don't try to parse this because dj_database_url will choke
        DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}}
    else:
        DATABASES = {'default': dj_database_url.config()}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'pihub.db',
            }
    }

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(PROJECT_DIR, 'media'))
STATIC_ROOT = os.path.join(MEDIA_ROOT, 'static')
DEVELOP_MODE = bool(os.environ.get('DEVELOP_MODE', False))
BROKER_URL = os.environ.get('BROKER_URL', 'django://')


if 'EXTRA_APPS' in os.environ:
    INSTALLED_APPS += os.environ['EXTRA_APPS'].split(',')

DEBUG = os.environ.get('DEBUG', False) == 'True'
TEMPLATE_DEBUG = DEBUG

GITHUB_APP_ID = os.environ.get('GITHUB_APP_ID', '')
GITHUB_API_SECRET = os.environ.get('GITHUB_API_SECRET', '')
GITHUB_EXTENDED_PERMISSIONS = ['user:email']

if DEVELOP_MODE:
    # serve static content from the development server
    SERVE_MEDIA=True
