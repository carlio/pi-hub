#@PydevCodeAnalysisIgnore
from pihub.settings import *

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

FCGI=False
CELERY_LOG_LEVEL = 'DEBUG'
