from os import path
import logging
import logging.config

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('logger_myOtherLogger')

# set a logging level
logger.setLevel(logging.DEBUG)
