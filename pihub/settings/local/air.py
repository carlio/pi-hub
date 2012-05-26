#@PydevCodeAnalysisIgnore
from pihub.settings.local import *

BROKER_URL = "django://"

INSTALLED_APPS += ["kombu.transport.django"]

STATICFILES_DIRS += [
    '/Users/carlcrowder/code/pi-hub/pihub/static/'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pihub',
        'USER': 'pcode',
        'PASSWORD': 'passw3rd',
        'HOST': '',
        'PORT': '',
    }
}

CACHE_FOLDER = '/Users/carlcrowder/code/pi-hib/.pypicache'

DEBUG = True

from pihub.settings.post import *