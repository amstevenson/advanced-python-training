# pastebin.com/1xhwatwh

import logging
import logging.config
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('logger_myOtherLogger')  # or log_file_path

# set a logging level
logger.setLevel(logging.DEBUG)

logger.info('its nearly tea')
logger.warning('warning')
logger.critical('a critical thing')
