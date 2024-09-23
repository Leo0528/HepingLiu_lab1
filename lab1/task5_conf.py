import logging
import logging.config

# Load logging configuration from the file
logging.config.fileConfig('task5.conf', disable_existing_loggers=False)

# Example logger usage
logger = logging.getLogger('sampleLogger')
logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
