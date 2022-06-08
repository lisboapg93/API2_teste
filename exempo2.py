import logging

import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')

logging.getLogger('flask_cors').level = logging.DEBUG