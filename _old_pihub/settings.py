import django.conf.global_settings as defaults

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = []
MANAGERS = ADMINS
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = []
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = ( 'pihub.common.middleware.RedirectSetuptools',
                       'pihub.common.middleware.WaitForIndexFetch', ) + defaults.MIDDLEWARE_CLASSES 
ROOT_URLCONF = 'pihub.urls'
WSGI_APPLICATION = 'pihub.wsgi.application'
TEMPLATE_DIRS = ()
CELERYBEAT_SCHEDULER = "pihub.packages.scheduler.Scheduler"
CELERY_IMPORTS = ()
CELERY_LOG_LEVEL = 'WARN'
ADMIN_EDIT_RELEASE = False
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
    },
           
    'loggers': {
        'django.db.backends': {
            'handlers': ['null'],  # Quiet by default!
            'propagate': False,
            'level':'DEBUG',
        },
    }
}








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

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'x3uog*7=(4%njw763=9b9^9m^w_3xy571s91u^x1@m+t1to4#i'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'south',
    'haystack',
    'celery', 'djcelery',
    'pihub.common',
    'pihub.packages',
]

