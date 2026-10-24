import logging
from .config import app_config as app_config

logger = logging.getLogger(name=__name__)
logger.info('app package loaded')
